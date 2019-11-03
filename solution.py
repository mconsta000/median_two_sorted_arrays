class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        return 0.0

    def search(self, nums: [int], low: int, high: int, target: int) -> int:
        mid = (low + high) // 2

        if (low > high):
            return low
        elif target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return self.search(nums, mid+1, high, target)
        else:
            return self.search(nums, low, mid-1, target)

    def merge(self, nums1: [int], nums2: [int]):
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        median_index = (nums1_len + nums2_len) // 2

        i = t = 0
        while (i < nums2_len and t < nums1_len):
            t = self.search(nums1, t, nums1_len-1, nums2[i])
            
            if (t > nums1_len-1):
                return
            elif nums1[t] > nums2[i]:
                self.swap(nums1, t, nums2, i)
                t = t + 1
            else:
                i = i + 1

    def swap(self, nums1: [int], i1: int, nums2: [int], i2: int):
        nums1[i1],nums2[i2] = nums2[i2],nums1[i1]


    def split(self, nums: [int]) -> [[int]]:
        mid_point = len(nums) // 2

        if mid_point == 0:
            return [nums, []]
        else:
            return [nums[:mid_point], nums[mid_point:]]