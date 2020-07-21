"""Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        st = 0
        en = len(nums) - 1
        while(st <= en):
            mid = (st + en) // 2

            if(nums[mid] == target):
                return mid

            if (nums[st] <= nums[mid]):
                if nums[st] <= target <= nums[mid]:
                    en = mid - 1
                else:
                    st = mid + 1
            else:
                if nums[mid] <= target <= nums[en]:
                    st = mid + 1
                else:
                    en = mid - 1

        return -1
