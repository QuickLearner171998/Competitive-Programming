class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if not nums[i]:
                nums[i] = -1
        prefix_sum = [nums[0]]
        ans=0
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1]+nums[i])
        for i in range(len(nums)-1, -1, -1):
            if prefix_sum[i]==0:
                ans = i+1
                break
        # if no zeros
        last_rep={num:i for i, num in enumerate(prefix_sum)}
        for i in range(len(prefix_sum)):
            if prefix_sum[i] in last_rep:
                ans = max(ans, last_rep[prefix_sum[i]]-i)
        return ans
        