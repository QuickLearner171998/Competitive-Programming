"""

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

"""


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        q = []
        minL = 1000000000
        for i in range(len(nums)):
            q.append(nums[i])
            if sum(q) >= s:
                while(sum(q) >= s):
                    minL = min(minL, len(q))
                    q.pop(0)
        if minL == 1000000000:
            minL = 0
        return minL
