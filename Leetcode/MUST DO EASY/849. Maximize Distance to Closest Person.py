class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        imax = pow(10, 5)
        leftNearestOne = [-1]*len(seats)
        l = imax
        leftNearestOne[0] = imax
        if seats[0]:
            leftNearestOne[0] = -1
            l = 0
        for i in range(1, len(seats)):
            if seats[i]==0:
                leftNearestOne[i] = i - l
            else:
                l = i
        rone = imax
        
        for i in  range(len(seats)-1, -1, -1):
            if seats[i]==0:
                leftNearestOne[i] = min(leftNearestOne[i], rone - i)
            else:
                rone = i
        return max(leftNearestOne)
                