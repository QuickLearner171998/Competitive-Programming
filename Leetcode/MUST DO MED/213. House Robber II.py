class Solution:
    def rob(self, nums: List[int]) -> int:
        def _helper(nums):
            dp = [0]*(len(nums)+1)
            dp[0] = 0
            dp[1] = nums[0]
            for i in range(2, len(nums)+1):
                dp[i] = max(nums[i-1]+dp[i-2], dp[i-1])
            return dp[-1]
        if len(nums)==1:
            return nums[0]
        return max(_helper(nums[1:]), _helper(nums[:-1]))