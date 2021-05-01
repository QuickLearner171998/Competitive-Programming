class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d  = {}
        for word in strs:
            t = ''.join(sorted(word))
            if t in d:
                d[t].append(word)
            else:
                d[t] = [word]
        return list(d.values())