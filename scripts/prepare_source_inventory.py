#!/usr/bin/env python3
"""Prepare a review-only inventory from a local site catalog and CSV export.

This script never promotes a case, changes public indexes, or republishes CSV
traffic metrics. Its output contains source pointers and merge hints only.
"""
import argparse
import csv
import hashlib
import json
import subprocess
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

from validate_catalog import metadata

ROOT = Path(__file__).resolve().parents[1]
NON_REPOS = {'topics', 'orgs', 'search', 'features', 'trending', 'collections',
             'sponsors', 'marketplace', 'login', 'about'}


def repo_root(value):
    if not isinstance(value, str) or not value.strip():
        return None
    raw = value.strip()
    if '://' not in raw:
        raw = 'https://' + raw
    parsed = urlsplit(raw)
    parts = [unquote(part) for part in parsed.path.strip('/').split('/')]
    if (parsed.hostname or '').lower() not in {'github.com', 'www.github.com'}:
        return None
    if len(parts) < 2 or not parts[0] or not parts[1] or parts[0].lower() in NON_REPOS:
        return None
    return f'https://github.com/{parts[0]}/{parts[1].removesuffix(".git")}'


def load_csv_repositories(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.DictReader(stream))
    if not rows or 'URL' not in rows[0]:
        raise ValueError('Expected Similarweb landing-page CSV with URL column')
    roots = set()
    for row in rows:
        root = repo_root(row['URL'])
        if root:
            roots.add(root.lower())
    return len(rows), roots


def prepare(site_path, aliases_path, csv_path):
    site_bytes = site_path.read_bytes()
    site = json.loads(site_bytes)
    aliases = json.loads(aliases_path.read_text())
    csv_rows, csv_roots = load_csv_repositories(csv_path)
    published = {}
    for path in (ROOT / 'cases').glob('*.md'):
        case, _ = metadata(path.read_text())
        if case['status'] == 'verified':
            published[case['project_url'].lower().rstrip('/')] = case['slug']
    if len(published) != len([p for p in (ROOT / 'cases').glob('*.md') if metadata(p.read_text())[0]['status'] == 'verified']):
        raise ValueError('Duplicate published project identity')
    by_root = defaultdict(set)
    records = []
    for item in site:
        slug = item['slug']
        canonical = item.get('canonicalSlug') or aliases.get(slug) or slug
        github = repo_root(item.get('github')) or repo_root(item.get('sourceUrl'))
        key = github.lower() if github else None
        if key:
            by_root[key].add(canonical)
        records.append({
            'site_slug': slug,
            'canonical_site_slug': canonical,
            'site_alias': slug != canonical,
            'source_url': item.get('sourceUrl') or None,
            'github_repository': github,
            'csv_repository_match': key in csv_roots if key else False,
            'published_case_slug': published.get(key) if key else None,
            'review_status': 'matched_published_project' if key in published else 'not_reviewed_for_this_catalog',
        })
    site_roots = set(by_root)
    repo_collisions = {
        root: sorted(slugs) for root, slugs in by_root.items() if len(slugs) > 1
    }
    summary = {
        'website_input_records': len(site),
        'website_canonical_slugs': len({record['canonical_site_slug'] for record in records}),
        'website_alias_records': sum(record['site_alias'] for record in records),
        'website_distinct_github_repositories': len(site_roots),
        'website_records_with_csv_repository_match': sum(record['csv_repository_match'] for record in records),
        'website_records_matching_published_project': sum(bool(record['published_case_slug']) for record in records),
        'github_repositories_linked_to_multiple_site_slugs': len(repo_collisions),
        'csv_landing_page_rows': csv_rows,
        'csv_distinct_repository_roots': len(csv_roots),
        'csv_repository_roots_also_in_website': len(csv_roots & site_roots),
        'csv_repository_roots_already_published': len(csv_roots & set(published)),
    }
    try:
        site_revision = subprocess.check_output(
            ['git', '-C', str(site_path.parent.parent), 'rev-parse', 'HEAD'], text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        site_revision = 'UNKNOWN'
    return {
        'purpose': 'Review-only intake; no website status is inherited and no case is promoted.',
        'website_source': 'Jev-For-Agents/data/build-records.json',
        'website_source_sha256': hashlib.sha256(site_bytes).hexdigest(),
        'website_repository_revision': site_revision,
        'csv_source': 'User-provided Similarweb GitHub landing-page export; URLs only used for local matching.',
        'csv_sha256': hashlib.sha256(csv_path.read_bytes()).hexdigest(),
        'summary': summary,
        'repository_collisions_to_review': repo_collisions,
        'records': records,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site-json', required=True, type=Path)
    parser.add_argument('--aliases-json', required=True, type=Path)
    parser.add_argument('--similarweb-csv', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    result = prepare(args.site_json, args.aliases_json, args.similarweb_csv)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result['summary'], ensure_ascii=False, indent=2))
