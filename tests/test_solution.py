import unittest

from solution import Solution
from statistics import median

class SolutionTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runAssertion(self, a, b):
        self.assertEqual((median(a) + median(b)) / 2 , self.solution.findMedianSortedArrays(a,b))

    def test1(self):
        a = [1,3]
        b = [2]

        self.runAssertion(a,b)

    def test2(self):
        a = [1,2]
        b = [3,4]

        self.runAssertion(a,b)

    def test3(self):
        a = [2,4]
        b = [1,2,3,4,5,6,7,10,100]

        self.runAssertion(a,b)
        
if __name__ == '__main__':
    unittest.main()