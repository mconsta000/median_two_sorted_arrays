import heapq

class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        total_length = len(nums1) + len(nums2)
        midpoint = total_length // 2
        median = 0.0

        nums = nums1 + nums2
        heapq.heapify(nums)
        ksmallest = heapq.nsmallest(midpoint+1, nums)

        if (total_length % 2 == 0):
            median = (ksmallest[midpoint-1] + ksmallest[midpoint]) / 2
        else:
            median = ksmallest[midpoint]

        return median