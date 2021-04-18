class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        ans = 0
        i = 1
        while 1:
            t = (n//pow(5, i))
            if t==0:
                return ans
            ans += t
            i+=1