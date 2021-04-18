class Solution:
    def isHappy(self, n: int) -> bool:
        notHappy = set()
        while n:
            if n ==1:
                return True
            if n in notHappy:
                return False
            notHappy.add(n)
            t = 0
            for c in str(n):
                t = t + (int(c))**2
            n = t

    