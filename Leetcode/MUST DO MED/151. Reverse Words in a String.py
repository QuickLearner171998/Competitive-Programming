class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        st = 0

        words=[]
        end=st+1
        # if end>=n-1:
        #     return s[st:end+1]
        while end<n:
            if s[end]==' ' and s[st]==' ':
                st+=1
                end+=1        
            elif s[st]==' ':
                st+=1
            elif s[end]==' ' and s[st]!=' ':
                words.append(s[st:end])
                st=end+1
                end=st

            elif s[st] !=' ' and s[end]!=' ':
                if end==n-1:
                    words.append(s[st:end+1])
                end+=1
                    
        words.reverse()
        return " ".join(words)