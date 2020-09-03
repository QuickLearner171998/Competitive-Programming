"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.



Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

class Solution:

    def getLsp(self, st):
        lsp = [0] * len(st)
        j = 0
        i = 1
        while i < len(st):
            if st[i] == st[j]:
                lsp[i] = j + 1
                j += 1
                i += 1
            else:
                if j == 0:
                    lsp[i] = 0
                    i += 1
                else:
                    j = lsp[j - 1]
        return (lsp[-1])

    def repeatedSubstringPattern(self, s: str) -> bool:

        # Soln 1
        # add same string twice will create at least on  more occurence of s in result
        # remove 1st and last char becoz we do not want ans true becozz of org string
        return s in (s + s)[1:-1]

        # Soln 2
        if len(s) == len(set(s)):
            return 0
        lsp = self.getLsp(s)
        if lsp == 0:
            return 0
        remL = len(s) - lsp
        if len(s) % remL:
            return 0
        return 1
