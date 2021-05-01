class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # """
        #                     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        #     ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        # """
        # #This example we see repeated subproblems subproblems
        
        def checkWord(i, s):
            
            #BASE 
            if s[i:] in dp:
                return dp[s[i:]]
            # print()
            if s[i:] in wordSet:
                return True

            for j in range(i, len(s)):
                if s[i:j+1] in wordSet and checkWord(j+1, s):
                    dp[s[i:]] = 1
                    return True
            dp[s[i:]]=0
        dp = {}
        wordSet = set(wordDict)
        return checkWord(0, s)