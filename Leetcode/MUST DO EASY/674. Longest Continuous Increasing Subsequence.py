class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not len(nums):
            return  0
        maxl=1
        curl=1

        i = 0
        while i<len(nums)-1:
            if nums[i] < nums[i+1]:
                curl+=1
                maxl = max(maxl, curl)
                
            else:
                curl=1
                
            i+=1
        return maxl
            
        