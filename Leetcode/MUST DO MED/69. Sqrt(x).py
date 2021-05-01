class Solution:
    def mySqrt(self, x: int) -> int:
        if  not x:
            return 0
        if x<4:
            return 1
        st = 1
        end = x//2
        while st<=end:
            mid = (st+end)//2
            if mid*mid == x:
                return mid
            if mid*mid > x:
                end = mid-1
            else:
                st = mid+1
        return end