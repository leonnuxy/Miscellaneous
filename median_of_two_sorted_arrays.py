class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # nums1.length == m
        # nums2.length == n
        # 0 <= m <= 1000
        # 0 <= n <= 1000
        # 1 <= m + n <= 2000
        # -106 <= nums1[i], nums2[i] <= 106

        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        if length % 2 == 0:
            return (nums1[length // 2] + nums1[length // 2 - 1]) / 2
        else:
            return nums1[length // 2]
            
