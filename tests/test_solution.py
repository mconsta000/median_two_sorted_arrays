import unittest

from solution import Solution
from statistics import median

class SolutionTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runAssertion(self, a, b):
        self.assertEqual(median(a+b), self.solution.findMedianSortedArrays(a,b))

    def test1(self):
        a = [1,3]
        b = [2]

        self.runAssertion(a,b)

    def test2(self):
        a = [1,2]
        b = [3, 4]

        self.runAssertion(a,b)
        
if __name__ == '__main__':
    unittest.main()