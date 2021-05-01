class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        lastocc = {}
        # mainatin currlen, if a ch repeats check whether it last occured in between (i, i-currlen)
        # if yes then length becomes i-lastIndex
        # else increment the currLen
        currLen = 0
        for i,c in enumerate(s):
            lastInd = -1 if c not in lastocc else lastocc[c]
            if lastInd==-1 or i-currLen > lastInd:
                currLen+=1
                ans = max(ans, currLen)
            else:
                if lastInd!=-1:
                    currLen = i - lastInd
                    
            lastocc[c] = i
        return ans
