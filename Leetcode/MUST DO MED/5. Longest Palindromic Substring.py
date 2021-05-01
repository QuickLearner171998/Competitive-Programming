class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[st][end] represents if s[st:end+1] is a palindrome or not
        dp = [[0]*(len(s)) for _ in range(len(s))]
        ans = ""
        #Init
        # dp[i][i] = 1 (single char)
        # dp[i][i+1]= 1 if s[i] == s[i+1]
        for st in range(len(s)):
            for end in range(st, len(s)):
                if st==end:
                    dp[st][end] = 1
                    ans = s[st] if len(ans)<1 else ans
                if end - st ==1 and s[st]==s[end]:
                    dp[st][end] = 1
                    ans = s[st:end+1]
        # main loop
        # bulid dp table from small to big
        for st in range((len(s)-1), -1, -1):
            for end in range(st+1, len(s)):
                if s[st] == s[end] and dp[st+1][end-1]:
                    dp[st][end] = 1
                    if end-st+1 >= len(ans):
                        ans = s[st:end+1]
        return ans
                    
        
