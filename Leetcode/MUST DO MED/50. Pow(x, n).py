class Solution:
    def myPow(self, x: float, n: int) -> float:
        # BIT manip O(lg(n))
        # pow(3, 5) --> pow(3, 101(bin)) --> pow(3, 2^2 * 1 + 2^1 * 0 + 2^0 * 1) 
        if n<0:
            x = 1/x
            n = -1*n
        ans = 1
        while n:
            #fetch the last bit
            if n&1:
                ans=ans*x
            x = x*x
            n = n>>1 # n=n//2
        return ans
        
#         Recursion        
#         if not n:
#             return 1
#         if n<0:
#             return 1/self.myPow(x, -1*n)
#         if not n%2:
#             # if power is dicv by 2 then intead of calling rec on (x, n-1) we can do (x*x, n//2)
#             return self.myPow(x*x, n//2)
#         return x*self.myPow(x, n-1)
    