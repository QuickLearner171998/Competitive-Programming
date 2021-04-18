class Solution:
    def romanToInt(self, s: str) -> int:
        
        ans = 0
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        subs = set(['IV', 'IX', 'XC', 'XL', 'CD', 'CM'] )
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i]+s[i+1] in subs:
                ans+=(d[s[i+1]] - d[s[i]])
                i+=1
            else:
                ans+=d[s[i]]
            i+=1
        return ans
            