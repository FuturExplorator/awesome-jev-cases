"""Regression checks for publication boundaries; no network or model calls."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from validate_catalog import ROOT, validate


class PublicationBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        self.case = self.root / 'cases/clearjev.md'

    def edit(self, before, after):
        self.case.write_text(self.case.read_text().replace(before, after))

    def assert_fails(self, fragment):
        errors, _ = validate(self.root)
        self.assertTrue(any(fragment in e for e in errors), errors)

    def test_valid_catalog(self):
        errors, count = validate(self.root)
        self.assertEqual(errors, [])
        self.assertGreater(count, 0)

    def test_unreviewed_cannot_remain_indexed(self):
        self.edit('status: "verified"', 'status: "under_review"')
        self.assert_fails('non-verified indexed')

    def test_compatible_only_cannot_be_verified(self):
        self.edit('jev_relation: "uses_typesafe"', 'jev_relation: "compatible_only"')
        self.assert_fails('requires concrete TypeSafe')

    def test_duplicate_project_url(self):
        self.edit('project_url: "https://github.com/huncijr/ClearJev"',
                  'project_url: "https://github.com/JKUDISH/jev-mcp.git/"')
        self.assert_fails('duplicate project_url')

    def test_independent_test_claim_needs_receipt(self):
        self.edit('claim_status: "source_reviewed"', 'claim_status: "independently_tested"')
        self.assert_fails('independent test evidence missing')

    def test_source_failure_cannot_pass(self):
        p = self.root / 'research/evidence/clearjev.json'
        d = json.loads(p.read_text()); d['sources'][0]['status'] = 404
        p.write_text(json.dumps(d))
        self.assert_fails('unsuccessful source retrieval')

    def test_missing_license_and_bilingual_section(self):
        (self.root / 'THIRD_PARTY_NOTICES.md').unlink()
        self.edit('### Evidence and limitations', '### Unspecified')
        self.assert_fails('missing bilingual section')
        self.assert_fails('missing THIRD_PARTY_NOTICES.md')


if __name__ == '__main__':
    unittest.main()
