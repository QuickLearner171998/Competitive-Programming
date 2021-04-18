class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified_once = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                if  modified_once:
                    return 0
                if i-1>=0:
                    if nums[i-1] > nums[i+1]:
                        nums[i+1] = nums[i]
                    else :
                        nums[i] = nums[i-1]
                else:
                    nums[i]=nums[i+1]
                modified_once = 1
                    
                    
        return 1