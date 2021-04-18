class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return 0
        s1 = {}
        s2 = {}
        for c1,c2 in zip(s,t):
            if c1 in s1:
                s1[c1]+=1
            else:
                s1[c1] = 1
            if c2 in s2:
                s2[c2]+=1
            else:
                s2[c2]=1
        
        
        for c, d in zip(s, t):
            if c not in s2 or d not in s1:
                return False
            if  s1[c] != s2[c] or s1[d]!=s2[d]:
                return False
        return True