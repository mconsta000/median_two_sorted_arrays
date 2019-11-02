class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        nums = self.merge(nums1, nums2)
        nums_len = len(nums)
        mid_point = nums_len // 2

        if nums_len % 2 == 0:
            return (nums[mid_point-1] + nums[mid_point]) / 2
        else:
            return nums[mid_point]

    def merge(self, nums1: [int], nums2: [int]) -> [int]:
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        if nums1_len == 0 or nums2_len == 0:
            return nums1 + nums2
        elif nums1[nums1_len-1] <= nums2[0]:
            return nums1 + nums2
        elif nums2[nums2_len-1] <= nums1[0]:
            return nums2 + nums1
        else:
            split1 = self.split(nums1)
            split2 = self.split(nums2)
            
            return self.merge(split1[0], split2[0]) + self.merge(split1[1], split2[1])

    def split(self, nums: [int]) -> [[int]]:
        mid_point = len(nums) // 2

        if mid_point == 0:
            return [nums, []]
        else:
            return [nums[:mid_point], nums[mid_point:]]