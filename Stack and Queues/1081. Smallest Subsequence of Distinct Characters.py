"""
Return the lexicographically smallest subsequence of text that contains all the distinct characters of text exactly once.

Example 1:

Input: "cdadabcc"
Output: "adbc"
Example 2:

Input: "abcd"
Output: "abcd"
Example 3:

Input: "ecbacba"
Output: "eacb"
Example 4:

Input: "leetcode"
Output: "letcod"


Constraints:

1 <= text.length <= 1000
text consists of lowercase English letters.
"""


class Solution:
    def smallestSubsequence(self, text: str) -> str:
        s = text
        stk = []

        lastCount = [-1] * 26
        inStack = [0] * 26

        for i, ch in enumerate(s):
            lastCount[ord(ch) - ord("a")] = i

        for i, ch in enumerate(s):

            if inStack[ord(ch) - ord("a")]:
                continue
            while stk and stk[-1] > ch and i < lastCount[ord(stk[-1]) - ord("a")]:
                # print(stk)
                inStack[ord(stk.pop()) - ord("a")] = 0
            stk.append(ch)
            inStack[ord(ch) - ord("a")] = 1
        return "".join(stk)
