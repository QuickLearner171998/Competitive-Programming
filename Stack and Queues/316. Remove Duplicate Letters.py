"""Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # logic
        # maintain a stack of characters
        # if encounter a ch < stk[-1] we pop ch present in the stack if those ch are present after current
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
