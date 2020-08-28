"""Given an integer n and an integer array rounds. We have a circular track which consists of n sectors labeled from 1 to n. A marathon will be held on this track, the marathon consists of m rounds. The ith round starts at sector rounds[i - 1] and ends at sector rounds[i]. For example, round 1 starts at sector rounds[0] and ends at sector rounds[1]

Return an array of the most visited sectors sorted in ascending order.

Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction (See the first example).

Example 1:


Input: n = 4, rounds = [1,3,1,2]
Output: [1,2]
Explanation: The marathon starts at sector 1. The order of the visited sectors is as follows:
1 --> 2 --> 3 (end of round 1) --> 4 --> 1 (end of round 2) --> 2 (end of round 3 and the marathon)
We can see that both sectors 1 and 2 are visited twice and they are the most visited sectors. Sectors 3 and 4 are visited only once.
"""

"""Explanation -

Case 1 :
if rounds[0] <= rounds[-1] in this case if some rounds have been completed then we just need to count from start(rounds[0]) to end(rounds[1]) as for complete rounds the count for each sector is same. and if the round is not complete then that means the count for each sector in between is 1.

Case 2:
rounds[0] > rounds[-1]
In this case also if some rounds have been completed then we just need to count from start(rounds[0]) to end(rounds[1]) the only difference is now we first need to count from rounds[0] to n and then from 1 to rounds[-1] and if the round is not complete then that means the count for each sector in between is 1.
"""


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        visited = [0] * n
        st = rounds[0]
        end = rounds[-1]

        if st <= end:
            return list(range(st, end + 1))

        return list(range(1, end + 1)) + list(range(st, n + 1))
