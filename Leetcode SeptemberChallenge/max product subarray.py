"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prevNeg = 1
        prevPos = 1
        currNeg = 1
        currPos = 1
        ans =  nums[0]
        n = len(nums)
        for i in range(n):
            # if nums[i] < 0:
            currPos = max(nums[i], nums[i]* prevNeg, nums[i]*prevPos )
            # else:
            ans = max(ans, currPos)
            currNeg = min(nums[i], nums[i]* prevNeg, nums[i]*prevPos)
            prevPos = currPos
            prevNeg = currNeg
        return ans