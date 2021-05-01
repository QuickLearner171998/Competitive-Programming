class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        st = end = 0
        inc = [st]
        dec = [st]
        
        ans = 0
        while end<len(nums):
            # Check if nums[end] can be min or max
            #INC
            while inc and nums[inc[-1]] >= nums[end]:
                inc.pop()
            inc.append(end)
            while dec and nums[dec[-1]] <= nums[end]:
                dec.pop()
            dec.append(end)
            # print("MIN", inc)
            # print("MAX", dec)
            # print()
            mini = nums[inc[0]]
            maxi = nums[dec[0]]
            if maxi-mini <= limit:
                ans = max(ans, end-st+1)
                end+=1
            else:
                st+=1
                if st > inc[0] : inc.pop(0)
                if st > dec[0] : dec.pop(0)      
                
        return ans
                
                
                
        
