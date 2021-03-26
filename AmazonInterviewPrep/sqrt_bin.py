class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        st = 1
        
        end = x//2 
        ans = 0
        while st<=end:
            mid = (st+end)//2
            if x/mid == mid:
                return mid
            if x/mid < mid:
                end = mid-1
            else:
                ans = mid
                st = mid+1
        return ans
                