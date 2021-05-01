class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            i1 = ans[-1]
            i2 = intervals[i]
            if i1[1] >= i2[0]:
                # can merge
                ans[-1][1] = max(i1[1], i2[1])
            else:
                ans.append(i2)
        return ans 
            