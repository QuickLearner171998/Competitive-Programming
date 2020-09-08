"""Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
"""


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        stri = str.split()
        if len(pattern)!=len(stri):
            return False


        stri = str.split()
        bij = {}
        invbij = {}
        # val_taken = {}
        for i in range(len(stri)):
            # print(bij)
            if stri[i] in bij:
                if bij[stri[i]] != pattern[i]:
                    return False
            else:
                bij[stri[i]] = pattern[i]
        f = 1
        bij = {}
        for i in range(len(stri)):
            # print(bij)
            if pattern[i] in bij:
                if bij[pattern[i]] != stri[i]:
                    return False
            else:
                bij[pattern[i]] = stri[i]
        return f and True

