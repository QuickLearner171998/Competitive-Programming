class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxTillNow = -1000000
        ans = -1000000
        sm = 0
        for n in nums:
            sm+=n
            if sm >= maxTillNow:
                maxTillNow = sm
                ans = max(ans, maxTillNow)
            if sm<0:
                sm = 0
        return ans
