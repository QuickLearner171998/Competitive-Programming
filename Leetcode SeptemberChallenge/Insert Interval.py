class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        leftList, rightList=[],[]
        START,END=0,1

        for currentInterval in intervals:
            if currentInterval[END]< newInterval[START]:
                leftList+= [currentInterval]

            elif currentInterval[START]> newInterval[END]:
                rightList+=[currentInterval]

            else:
                newInterval[START]= min(currentInterval[START],newInterval[START])
                newInterval[END]= max(currentInterval[END], newInterval[END])

        return leftList + [[newInterval[START], newInterval[END]]] + rightList
