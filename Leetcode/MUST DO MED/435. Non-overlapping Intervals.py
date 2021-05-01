class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort acct to end time ---> see this case (1,100), (2, 3), (4,5)
        intervals.sort(key = lambda x:x[1])
        ans = 0
        st = 0
        end = 1
        while end < len(intervals):
            if intervals[st][1] <= intervals[end][0]:
                # CANT merge
                st=end
                end+=1
            else:
                end = end+1
                ans+=1
        return ans
            