#!/usr/bin/env python3
"""Offline, read-only checks. Passing does not grant source verification."""
import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'(?<!!)\[[^\]\n]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)')
HEADINGS = ['## 中文', '### 项目简介', '### Jev 的具体作用', '### 如何复现',
            '### 证据与限制', '## English', '### Overview', "### Jev's specific role",
            '### Reproduction', '### Evidence and limitations', '## Sources / 来源']


def metadata(text):
    if not text.startswith('---\n'):
        raise ValueError('missing front matter')
    front, body = text[4:].split('\n---\n', 1)
    result = {}
    for line in front.splitlines():
        key, value = line.split(': ', 1)
        if key in result:
            raise ValueError('duplicate metadata key: ' + key)
        result[key] = json.loads(value)
    return result, body


def identity(url):
    u = urlsplit(url)
    return (u.hostname or '').lower() + u.path.rstrip('/').removesuffix('.git').lower()


def validate(root=ROOT):
    errors = []
    def check(ok, message):
        if not ok:
            errors.append(message)
    schema = json.loads((root / 'schema/case.schema.json').read_text())
    props = schema['properties']
    cases, projects, sources, repo_ids = {}, {}, {}, {}
    for path in sorted((root / 'cases').glob('*.md')):
        try:
            m, body = metadata(path.read_text())
            for k in schema['required']:
                check(k in m, f'{path.name}: missing {k}')
            for k, v in m.items():
                check(k in props, f'{path.name}: unknown field {k}')
                if k not in props:
                    continue
                spec = props[k]
                check(isinstance(v, str) and bool(v), f'{path.name}: {k} must be a nonempty string')
                if not isinstance(v, str):
                    continue
                if 'enum' in spec:
                    check(v in spec['enum'], f'{path.name}: invalid {k}')
                if 'pattern' in spec:
                    check(re.search(spec['pattern'], v) is not None, f'{path.name}: invalid {k} pattern')
            slug = m['slug']
            check(path.stem == slug, f'{path.name}: slug/filename mismatch')
            check(slug not in cases, f'duplicate slug: {slug}')
            cases[slug] = m
            for field, seen in [('project_url', projects), ('source_url', sources)]:
                key = identity(m[field])
                check(key not in seen, f'{slug}: duplicate {field} with {seen.get(key)}')
                seen[key] = slug
            for field in ('last_checked', 'source_date'):
                if m[field] != 'UNKNOWN':
                    date = dt.date.fromisoformat(m[field])
                    check(date <= dt.datetime.now(dt.timezone.utc).date(), f'{slug}: future {field}')
            if m['source_date'] == 'UNKNOWN':
                check(m['source_date_kind'] == 'unknown', f'{slug}: unknown date needs unknown kind')
            if m['source_kind'] == 'github':
                check(re.fullmatch(r'[0-9a-f]{40}', m.get('source_revision', '')) is not None,
                      f'{slug}: GitHub revision required')
                check(m['source_url'].startswith(m['project_url'] + '/blob/' + m.get('source_revision', '') + '/'),
                      f'{slug}: source must be pinned to project revision')
            for heading in HEADINGS:
                check(heading in body.splitlines(), f'{slug}: missing bilingual section {heading}')
                if heading in body and heading not in ('## 中文', '## English'):
                    section = body.split(heading, 1)[1].split('\n#', 1)[0].strip()
                    check(bool(section), f'{slug}: empty section {heading}')
            check(re.search(r'[\u4e00-\u9fff]', body.split('## English')[0]) is not None,
                  f'{slug}: Chinese text missing')
            if m['status'] != 'verified':
                continue
            check(m['jev_relation'] == 'uses_typesafe', f'{slug}: verified requires concrete TypeSafe use')
            check(m['claim_status'] in ('source_reviewed', 'independently_tested'), f'{slug}: author report alone')
            check(not any(x in body for x in ['REPLACE', '待填写']), f'{slug}: placeholder content')
            receipt_path = (root / m['evidence_file']).resolve()
            check(receipt_path.is_relative_to(root.resolve()), f'{slug}: receipt escapes repository')
            if not receipt_path.is_relative_to(root.resolve()):
                continue
            d = json.loads(receipt_path.read_text())
            for field in ('slug', 'project_url', 'claim_status', 'upstream_license'):
                check(d.get(field) == m[field], f'{slug}: receipt mismatch {field}')
            for field in ('reviewer', 'review_method', 'runtime_test', 'performance_test', 'checked_at'):
                check(bool(d.get(field)), f'{slug}: missing receipt {field}')
            check(d['checked_at'][:10] == m['last_checked'], f'{slug}: receipt date mismatch')
            if m['source_kind'] == 'github':
                check(d.get('public') is True, f'{slug}: repository not public')
                check(d.get('revision') == m['source_revision'], f'{slug}: receipt revision mismatch')
                check(d.get('owner') == m['author'], f'{slug}: owner attribution mismatch')
                check(d.get('revision_date', '')[:10] == m['source_date'], f'{slug}: commit date mismatch')
                rid = d.get('repository_id')
                check(isinstance(rid, int) and rid not in repo_ids, f'{slug}: missing/duplicate repository id')
                repo_ids[rid] = slug
            check(bool(d.get('sources')), f'{slug}: no sources in receipt')
            for source in d.get('sources', []):
                check(source.get('status') == 200, f'{slug}: unsuccessful source retrieval')
                check(re.fullmatch(r'[a-f0-9]{64}', source.get('sha256', '')) is not None, f'{slug}: missing hash')
                check(bool(source.get('inspected_scope')), f'{slug}: missing inspected scope')
                check(source.get('checked_at', '')[:10] == m['last_checked'], f'{slug}: source check date mismatch')
                if m['source_kind'] == 'github':
                    prefix = m['project_url'].replace('https://github.com/', 'https://raw.githubusercontent.com/')
                    prefix += '/' + m['source_revision'] + '/'
                    check(source.get('url') == prefix + source.get('path', ''), f'{slug}: mismatched captured source')
            if m['claim_status'] == 'independently_tested':
                check(d.get('runtime_test') == 'passed' and bool(d.get('test_record')), f'{slug}: independent test evidence missing')
            if 'website_url' in m:
                check(any(s.get('url') == m['website_url'] and s.get('status') == 200 for s in d.get('website_checks', [])),
                      f'{slug}: website page not checked')
        except (ValueError, KeyError, OSError, TypeError) as exc:
            errors.append(f'{path.name}: {exc}')
    indexed = []
    for page in (root / 'categories').glob('*.md'):
        for slug in re.findall(r'\]\(\.\./cases/([a-z0-9-]+)\.md\)', page.read_text()):
            indexed.append(slug)
            check(slug in cases and cases[slug]['status'] == 'verified', f'{page.name}: non-verified indexed {slug}')
            if slug in cases:
                check(cases[slug]['scenario'] == page.stem, f'{slug}: wrong category')
    expected = sorted(k for k, v in cases.items() if v['status'] == 'verified')
    check(sorted(indexed) == expected, 'category membership is missing, duplicated or not verified')
    readme = (root / 'README.md').read_text()
    check(f'现有目录：{len(expected)} 个独立项目' in readme and f'Current catalog: {len(expected)} distinct projects' in readme,
          'README counts do not match verified cases')
    for slug in re.findall(r'\]\(cases/([a-z0-9-]+)\.md\)', readme):
        check(slug in expected, f'README promotes non-verified case {slug}')
    ledger = json.loads((root / 'research/candidates.json').read_text())
    check(len({c['id'] for c in ledger}) == len(ledger), 'duplicate candidate ids')
    check(sorted(c['id'] for c in ledger if c['status'] == 'verified') == expected, 'candidate/public status drift')
    attribution = (root / 'research/ATTRIBUTION.md').read_text()
    check(sorted(re.findall(r'\]\(\.\./cases/([a-z0-9-]+)\.md\)', attribution)) == expected, 'attribution coverage mismatch')
    for required in ['LICENSE', 'THIRD_PARTY_NOTICES.md', 'CONTRIBUTING.md', 'GOVERNANCE.md', '.github/ISSUE_TEMPLATE/case.yml']:
        check((root / required).is_file(), 'missing ' + required)
    if (root / 'LICENSE').is_file():
        check('Copyright (c) 2026 FuturExplorator and contributors' in (root / 'LICENSE').read_text(), 'license owner mismatch')
    for path in root.rglob('*.md'):
        if '.git' in path.parts:
            continue
        text = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for link in LINK.findall(text):
            u = urlsplit(link.strip('<>'))
            if u.scheme or u.netloc:
                continue
            target = (path.parent / unquote(u.path)).resolve() if u.path else path
            check(target.exists(), f'{path.relative_to(root)}: broken local link {link}')
            if target.is_file() and target.suffix == '.md' and u.fragment:
                headings = re.findall(r'^#+\s+(.+)$', target.read_text(), re.M)
                anchors = [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings]
                check(unquote(u.fragment) in anchors, f'{path.name}: missing anchor {link}')
    return errors, len(expected)


if __name__ == '__main__':
    failures, count = validate()
    if failures:
        print('\n'.join('FAIL: ' + x for x in failures))
        sys.exit(1)
    print(f'PASS: {count} verified cases; metadata, identities, receipts, status/index/attribution parity and local links.')
    print('Offline checks only; source truth, bilingual semantics and live links require review.')
