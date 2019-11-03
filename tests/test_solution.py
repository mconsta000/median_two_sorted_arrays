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

    def test_split3(self):
        self.assertEqual(self.solution.split([1]), [[1],[]])

    def test_merge1(self):
        a = [1]
        b = []
        self.solution.merge(a,b)
        self.assertEqual(a, [1])
        self.assertEqual(b, [])

    def test_merge2(self):
        a = []
        b = [1]
        self.solution.merge(a,b)
        self.assertEqual(a, [])
        self.assertEqual(b, [1])

    def test_merge3(self):
        a = [1]
        b = [2]
        self.solution.merge(a,b)
        self.assertEqual(a, [1])
        self.assertEqual(b, [2])

    def test_merge4(self):
        a = [2]
        b = [1]
        self.solution.merge(a,b)
        self.assertEqual(a, [1])
        self.assertEqual(b, [2])

    def test_merge6(self):
        a = [1,3]
        b = [2]
        self.solution.merge(a,b)
        self.assertEqual(a, [1,2])
        self.assertEqual(b, [3])

    def test_merge7(self):
        a = [3]
        b = [2,4]
        self.solution.merge(a,b)
        self.assertEqual(a, [2])
        self.assertEqual(b, [3,4])

    def test_merge8(self):
        a = [2,2]
        b = [2,3]
        self.solution.merge(a,b)
        self.assertEqual(a, [2,3])
        self.assertEqual(b, [2,3])

    def test_merge9(self):
        a = [2]
        b = [1,3]
        self.solution.merge(a,b)
        self.assertEqual(a, [1,2])
        self.assertEqual(b, [3])

    def test_merge10(self):
        a = [1,4]
        b = [2,3]
        self.solution.merge(a,b)
        self.assertEqual(a, [1,2])
        self.assertEqual(b, [3,4])

    def test_merge11(self):
        a = [2]
        b = [1,3,4,5]
        self.solution.merge(a,b)
        self.assertEqual(a, [1])
        self.assertEqual(b, [2,3,4,5])

    def test_merge12(self):
        a = [1,2,3,5]
        b = [4]
        self.solution.merge(a,b)
        self.assertEqual(a, [1,2,3,4])
        self.assertEqual(b, [5])

    def test_merge13(self):
        a = [1,2,3,6]
        b = [4,5]
        self.solution.merge(a,b)
        self.assertEqual(a, [1,2,3,4])
        self.assertEqual(b, [5,6])

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

        while i < 1000000:
            if (i % 2 == 0):
                a.append(i)
            else:
                b.append(i)

            i=i+1

        self.runAssertion(a,b)

    def runSearch(self, nums: [int], target: int, expected: int):
        self.assertEqual(self.solution.search(nums, 0, len(nums)-1, target), expected)

    def test_search1(self):
        a = [0,1,2,5]
        self.runSearch(a, 1, 1)

    def test_search2(self):
        a = [0,1,2,5,7]
        self.runSearch(a, 2, 2)

    def test_search3(self):
        a = [0,1,2,5,7]
        self.runSearch(a, 7, 4)

    def test_search4(self):
        a = [0,1,2,5,7]
        self.runSearch(a, 0, 0)

    def test_search5(self):
        a = [0,1,2,5,7]
        self.runSearch(a, 2, 2)

    def test_search6(self):
        a = [0,1,2,3,4,5,6,7,8,9,10,11,12]
        self.runSearch(a, 10, 10)

    def test_search7(self):
        a = [0,1,2,3,4,5,6,7,8,9,10,11,12]
        self.runSearch(a, 13, 13)

    def test_search8(self):
        a = [0,2,3,4,5,6,7,8,9,10,11,12]
        self.runSearch(a, 1, 1)

    def test_search9(self):
        a = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.runSearch(a, 0, 0)


if __name__ == '__main__':
    unittest.main()