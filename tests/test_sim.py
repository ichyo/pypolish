import unittest
import pypolish


class TestSimilarity(unittest.TestCase):
    def test_jaccard_index(self):
        res = pypolish.jaccard_index(1, 2, 3, 5)
        self.assertAlmostEqual(res, 1.0 / 4.0)

    def test_jaccard_index_fail(self):
        self.assertRaises(ValueError, pypolish.jaccard_index, -1, 2, 3, 5)
