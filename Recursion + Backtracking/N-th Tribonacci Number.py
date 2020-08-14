"""The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 """


class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def memoiz(n, memo):
            if n == 0 or n == 1:
                return n
            if n == 2:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = memoiz(n - 3, memo) + memoiz(n - 2, memo) + memoiz(n - 1, memo)
            return memo[n]

        return memoiz(n, memo)
