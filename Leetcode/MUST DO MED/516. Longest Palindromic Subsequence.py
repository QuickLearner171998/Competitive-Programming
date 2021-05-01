class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def createDp(s1, s2):
            dp = [[0]*(len(s1)+1) for _ in range(len(s1)+1)]
            for i in range(1, len(s1)+1):
                for j in range(1, len(s1)+1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            return dp
        def createSeq(s1, s2, dp):
            ans = ''
            i , j = len(s1), len(s2)
            f = 0
            while i>0:
                if dp[i][j]==0:
                    f = 1
                    break  
                while j>0:
                    if dp[i][j]==0:
                        f = 1
                        break  
                        
                    if s1[i-1]==s2[j-1]:
                        ans+= s1[i-1]
                        i=i-1
                        j=j-1
                    else:
                        if dp[i-1][j] >= dp[i][j-1]:
                            i=i-1
                        else:
                            j=j-1
                if f:
                    break
            return ans
        srev = s[::-1]
        dp = createDp(s, srev)
        return (dp[-1][-1])
        # return createSeq(s, srev, dp)
                