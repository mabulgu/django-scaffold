from django.test import TransactionTestCase
from django.test.runner import DiscoverRunner
from unittest.suite import TestSuite
from django_nose import NoseTestSuiteRunner


class UnitTestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        pass

    def teardown_databases(self, old_config, **kwargs):
        pass

    def build_suite(self, test_labels=None, extra_tests=None, **kwargs):
        suite = super().build_suite(**kwargs)
        tests = [t for t in suite._tests if self.is_unittest(t)]
        return TestSuite(tests=tests)

    @staticmethod
    def is_unittest(test):
        return not issubclass(test.__class__, TransactionTestCase)


class NoseUnitTestSuiteRunner(NoseTestSuiteRunner):
    def setup_databases(self, **kwargs):
        pass

    def teardown_databases(self, old_config, **kwargs):
        pass

    def build_suite(self, test_labels=None, extra_tests=None, **kwargs):
        suite = super().build_suite(**kwargs)
        tests = [t for t in suite._tests if self.is_unittest(t)]
        return TestSuite(tests=tests)

    @staticmethod
    def is_unittest(test):
        return not issubclass(test.__class__, TransactionTestCase)
