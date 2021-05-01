class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def multi(l1, s2):
            ans = []
            for word in l1:
                for c2 in s2:
                    ans.append(word+c2)
            return ans
        if len(digits)==0:
            return []
        letters = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        ans = []
        temp = list(letters[int(digits[0])])
        ans = temp
        for d in digits[1:]:
            word = letters[int(d)]
            ans = multi(temp, word)
            temp = ans
        return (ans)