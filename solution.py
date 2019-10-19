import math

class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:        
        r1 = self.reduce(nums1)
        r2 = self.reduce(nums2)

        return (r1+r2) / 2

    def reduce(self, nums: [int]) -> float:
        s = len(nums)

        if s == 1:
            return nums[0]
        elif s == 2:
            return (nums[0] + nums[1]) / 2
        else:
            i = math.ceil(s / 2)
            if s % 2 == 1:
                return nums[i-1]
            else:
                return (nums[i-1:i] + nums[i:i+1]) / 2

        return 0.0