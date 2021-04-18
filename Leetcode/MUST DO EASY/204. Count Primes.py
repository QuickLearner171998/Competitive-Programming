class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [0]*(n)
        if n>2:
            primes[2] = 1
        for i in range(3, n, 2):
            primes[i] = 1
        for i in range(3, n, 2):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = 0
        ans = 0
        for p in primes:
            if p:
                ans+=1
        return ans