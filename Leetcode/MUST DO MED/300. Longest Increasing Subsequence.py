class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*(len(nums))
        for i in range(1, len(nums)):
            
            #j < i
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(1+dp[j], dp[i])
        # print(dp)
        return max(dp)