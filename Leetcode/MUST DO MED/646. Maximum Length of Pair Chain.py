class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if len(pairs)<2:
            return len(pairs)
        pairs.sort(key=lambda x:x[1])
        print(pairs)
        ans=0
        last_end = -10000
        i=0
        while i<len(pairs):
            st, end = pairs[i]
            if last_end < st:
                last_end = end
                ans+=1
            i+=1
        return ans
            
            
            