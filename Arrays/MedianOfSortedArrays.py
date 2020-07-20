"""

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

"""



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        st = 0
        en = len(nums1)

        while(st <=en):
            p = (len(nums1) + len(nums2) + 1)//2
            p1 = (en+st)//2
            p2 = p - p1
            if p1 == 0:
                a1L = -10000000000
            else:
                a1L = nums1[p1 - 1]
            if p1 == len(nums1):
                a1R = 100000000000
            else:
                a1R = nums1[p1]


            if p2 == 0:
                a2L = -10000000000
            else:
                a2L = nums2[p2 - 1]
            if p2 == len(nums2):
                a2R = 10000000000000
            else:
                a2R = nums2[p2]


            if (a1L <= a2R) and (a2L <= a1R):

                if (len(nums1) + len(nums2)) % 2:
                    return max(a1L, a2L)
                else:
                    return (max(a1L, a2L) + min(a1R, a2R)) / 2

            elif a1L > a2R:
                en = p1 - 1

            else:
                st = p1 + 1
