class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {chr(c):-1 for c in range(ord('a'),ord('z')+1)}
        for i in range(len(s)):
            if d[s[i]]==-1:
                d[s[i]] = i
            else:
                d[s[i]] = -2
        ans = 100002
        for c in d:
            if d[c]>=0:
                ans = min(ans, d[c])
        return ans if ans!=100002 else -1