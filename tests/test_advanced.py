# -*- coding: utf-8 -*-

from .context import sample
from sample.util.data import Junk


from unittest import TestCase


class AdvancedTestSuite(TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(sample.hmm())

    def test_junk(self):
        j = Junk()
        self.assertEqual("we stuff", j.stuff())
