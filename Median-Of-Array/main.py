class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_num = sorted(nums1 + nums2)
        size_num = len(merged_num)
        median = 0
        if(size_num % 2 == 1):
            return float(merged_num[size_num // 2])
        else:
            mid = size_num // 2
            return (merged_num[mid-1] + merged_num[mid]) / 2.0
