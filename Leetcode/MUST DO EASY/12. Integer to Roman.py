class Solution:
    def intToRoman(self, num: int) -> str:
        ans = 0
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        subs = set(['IV', 'IX', 'XC', 'XL', 'CD', 'CM'] )
        for rmn in subs:
            d[rmn] = d[rmn[1]] - d[rmn[0]]        
        
        d = {val:key for key, val in d.items()}
        
        if num in d:
            return d[num]
        d = {key : val for key, val in sorted(d.items(), key = lambda x:x[0], reverse = True) }
        ans = ''
        while num > 0:
            if num in d:
                ans+= d[num]
                break
            else:
                # find just smaller
                for key in d:
                    if key <= num:
                        ans+=d[key]
                        num-=key
                        break
        
        # print(ans)
        return ans