import unittest

from solution import Solution
from statistics import median

class SolutionTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runAssertion(self, a, b):
        self.assertEqual((median(a + b)) , self.solution.findMedianSortedArrays(a,b))

    def test_split1(self):
        self.assertEqual(self.solution.split([1,2,3]), [[1],[2,3]])

    def test_split2(self):
        self.assertEqual(self.solution.split([1,2,3,4]), [[1,2],[3,4]])

    def test_split2(self):
        self.assertEqual(self.solution.split([1]), [[],[1]])

    def test_merge1(self):
        self.assertEqual(self.solution.merge([1], []), [1])

    def test_merge2(self):
        self.assertEqual(self.solution.merge([], [1]), [1])

    def test_merge3(self):
        self.assertEqual(self.solution.merge([1], [2]), [1,2])

    def test_merge4(self):
        self.assertEqual(self.solution.merge([2], [1]), [1,2])

    def test_merge6(self):
        self.assertEqual(self.solution.merge([1,3], [2]), [1,2,3])

    def test_merge7(self):
        self.assertEqual(self.solution.merge([3], [2,4]), [2,3,4])

    def test_merge8(self):
        self.assertEqual(self.solution.merge([2,2], [2,3]), [2,2,2,3])

    def test_merge7(self):
        self.assertEqual(self.solution.merge([2], [1,3]), [1,2,3])

    def test_merge8(self):
        self.assertEqual(self.solution.merge([1,4], [2,3]), [1,2,3,4])

    def test_median1(self):
        a = [1,3]
        b = [2]

        self.runAssertion(a,b)

    def test_median2(self):
        a = [1,2]
        b = [3,4]

        self.runAssertion(a,b)

    def test_median3(self):
        a = [2,4]
        b = [1,2,3,4,5,6,7,10,100]

        self.runAssertion(a,b)

    def test_median4(self):
        a = [2,2,2,2]
        b = [4,4,4,4]

        self.runAssertion(a,b)

    def test_median5(self):
        i = 0
        a = []
        b = []

        while i < 10000:
            if (i % 2 == 0):
                a.append(i)
            else:
                b.append(i)

            i=i+1

        self.runAssertion(a,b)

if __name__ == '__main__':
    unittest.main()