class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        count = {c:0 for c in chars}
        for c in chars:
            count[c]+=1
        for word in words:
            not_include = 0
            
            wc= {c:0 for c in word}
            for c in word:
                wc[c]+=1            
            for c in word:
                if c not in count or  wc[c]>count[c]:
                    not_include=1
                    break
            if not not_include:
                ans+=len(word)
        return ans
                    
                
                
            
