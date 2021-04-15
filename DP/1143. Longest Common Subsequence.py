"""Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def printLCS(dp, s1, s2):
            n = len(s1)
            m = len(s2)
            s = ""
            while n > 0 and m > 0:
                if s1[n-1] == s2[m-1]:
                    s = s1[n-1]+s
                    n-=1
                    m-=1
                elif dp[n-1][m] > dp[n][m-1]:
                    n-=1
                else:
                    m-=1
            print(s)

        n = len(text1)
        m = len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # printLCS(dp, text1, text2)
        return dp[-1][-1]
            
                    
                    
        