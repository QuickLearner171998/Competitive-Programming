class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_occ = {s:i for i, s in enumerate(S)}
        
        ans = []
        partition = 0
        l = 0
        for i in range(len(S)):
            partition = max(partition, last_occ[S[i]])
            l+=1
            if i == partition:
                ans.append(l)
                l = 0
        return ans