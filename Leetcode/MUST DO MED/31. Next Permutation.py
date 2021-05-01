class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<=1:
            return 
        next_not_poss = 1
        # find first aooc of nums[i]>nums[i-1] from right
        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                next_not_poss = 0
                break
        # if reached end that means reverse sorted
        if next_not_poss:
            nums.sort()
        else:
            # swap nums[i-1] with number just greater than nums[i-1] on its right
            for j in range(n-1, i-1, -1):
                if nums[i-1] < nums[j]:
                    nums[i-1], nums[j] = nums[j], nums[i-1]
                    break
            # reverse the nums[i:]
            nums[i:] = reversed(nums[i:])
            
            