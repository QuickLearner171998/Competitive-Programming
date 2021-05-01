class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """https://www.youtube.com/watch?v=bdxJHWIyyqI"""
        ovf = 2147483647
        # overflow
        if dividend== -1*(ovf+1) and divisor==-1:
            return ovf
        if dividend==0:
            return 0
        #find highest power of 2 st dividend/pow(2,x) - div >0
        # a >> n == a//pow(2,n)
        # a<<n == a*pow(2,n)
        neg = 1
        if not ((dividend>0)==(divisor>0)): # check same sign
            neg = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        exp = 31
        q = 0
        while exp > -1:
            if (dividend >> exp)- divisor >=0:
                # the number by which dividend is reduced is essentially the quotient as this
                # can be written as dividend - divisor << exp >=0 or divid - div*(pow(2,exp)) >=0
                q += 1<<exp # q=q+ pow(2,exp)
                dividend -= divisor<<exp # dividend-= div*pow(2,exp)
            exp-=1
        return q*neg