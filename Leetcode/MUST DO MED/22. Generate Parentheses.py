class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        nOpen = n
        nClose = n
        def rec(s, nOpen, nClose, ans):
            if nOpen==0 and nClose==0:
                ans.append(s) 
            if nOpen<0 or nClose<0:
                return 
            if nClose - nOpen >=0:
                rec(s+'(', nOpen-1, nClose, ans)
                rec(s+')', nOpen, nClose-1, ans)
        
        ans = []
        rec('(', n-1, n, ans)
        return ans
    