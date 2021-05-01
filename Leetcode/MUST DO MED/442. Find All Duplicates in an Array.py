class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        from collections import Counter
        cnt = Counter(nums)
        ans = []
        for c in cnt:
            if cnt[c]==2:
                ans.append(c)
        return ans