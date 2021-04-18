class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n!=m:
            return 0
        
        d = {}
        tset = set()
        for i in range(n):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return 0
            else:
                if t[i] in tset:
                    return 0
                d[s[i]] = t[i]
            tset.add(t[i])
        return 1