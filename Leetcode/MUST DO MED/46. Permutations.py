class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def _helper(current, n):
            # BASE
            if current==n:
                ans.append(nums.copy())
                return ans
            for i in range(current, n):
                # swap i and current of array
                nums[i], nums[current]  = nums[current]  , nums[i]
                # now again run recursion on this array
                _helper(current+1, n)
                # after recursion again make the array originial
                nums[i], nums[current]  = nums[current]  , nums[i]

        ans = []
        _helper(0, len(nums))
        return ans