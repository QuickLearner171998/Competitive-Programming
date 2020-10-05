"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added."""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        c1 = Counter(s)
        c2 = Counter(t)

        # print(c1, c2)

        for c in t:
            if c not in s or c1[c] != c2[c]:
                return c
        return ""