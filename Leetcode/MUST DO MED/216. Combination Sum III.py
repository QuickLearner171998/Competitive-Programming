class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def _helper(st, n, k, temp):
            if n==0 and k==0:
                ans.append(temp[:])
            if n<0 or k<0:
                return
        
            for i in range(st, 10):
                temp.append(i)
                _helper(i+1, n-i, k-1, temp)
                temp.pop(-1)
        ans = []
        _helper(1, n, k, [])
        return ans 
            