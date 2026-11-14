#!/usr/bin/env python3
"""Ein kurzer aktiver Router darf keine erhaltenen Fachmodule ersetzen."""
import copy
import unittest
from ki_kanzlei_release_contract import (
    VERSION, ACTIVE_SKILL_COUNT, ACTIVE_SKILL_SLUGS, MODULE_COUNT, MODULE_SLUGS,
    minimum_pages, validate_module_report,
)


def fixture():
    rows = [{'skill': slug, 'pages': minimum_pages(slug)} for slug in sorted(MODULE_SLUGS)]
    return {'schema_version': 2, 'version': VERSION, 'active_skill_count': ACTIVE_SKILL_COUNT,
            'active_skills': sorted(ACTIVE_SKILL_SLUGS), 'module_count': MODULE_COUNT,
            'modules': rows, 'total_module_pages': sum(r['pages'] for r in rows)}


class UmfangsvertragTests(unittest.TestCase):
    def test_complete_original_modules_and_active_routes_are_distinct(self):
        report = fixture()
        self.assertEqual(len(validate_module_report(report)), 30)
        self.assertLessEqual(ACTIVE_SKILL_COUNT, 20)
        self.assertLess(ACTIVE_SKILL_COUNT, MODULE_COUNT)

    def test_previous_component_version_is_rejected(self):
        report = fixture()
        report['version'] = '445.35.2'
        with self.assertRaises(AssertionError):
            validate_module_report(report)

    def test_missing_original_cannot_be_hidden_by_adjusting_count(self):
        report = fixture()
        report['modules'].pop()
        report['module_count'] -= 1
        with self.assertRaises(AssertionError):
            validate_module_report(report)

    def test_short_route_cannot_replace_long_original(self):
        report = fixture()
        row = next(r for r in report['modules'] if minimum_pages(r['skill']) == 10)
        row['pages'] = 1
        report['total_module_pages'] = sum(r['pages'] for r in report['modules'])
        with self.assertRaises(AssertionError):
            validate_module_report(report)

    def test_duplicate_module_does_not_preserve_coverage(self):
        report = fixture()
        report['modules'][-1] = copy.deepcopy(report['modules'][0])
        with self.assertRaises(AssertionError):
            validate_module_report(report)

    def test_old_or_invented_active_skill_set_is_rejected(self):
        for active in (sorted(MODULE_SLUGS), sorted(ACTIVE_SKILL_SLUGS - {next(iter(ACTIVE_SKILL_SLUGS))}) + ['invented']):
            report = fixture()
            report['active_skills'] = active
            report['active_skill_count'] = len(active)
            with self.assertRaises(AssertionError):
                validate_module_report(report)


if __name__ == '__main__':
    unittest.main()
