"""Sequential Digits

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.



Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]


Constraints:

10 <= low <= high <= 10^9
"""


class Solution:
    def generateNums(self, digit, n):
        ans = 0
        while(n > 0):
            ans += digit * pow(10, n - 1)
            digit += 1
            n -= 1

        return ans

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        import math
        minlen = int(math.log10(low) + 1)
        maxlen = int(math.log10(high) + 1)
        ans = []

        l = minlen
        while l <= maxlen:
            for fdigit in range(1, 9 - l + 2):
                num = self.generateNums(fdigit, l)
                if num <= high and num >= low:
                    ans.append(num)
                # else:
                #     break
            l += 1
        return ans
