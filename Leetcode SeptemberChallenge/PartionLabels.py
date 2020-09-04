"""A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.



Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # if only 1 occurences of each
        if len(set(S)) == len(S):
            return [1] * len(S)
        # dict of LastIndex
        lastInd = {c: i for i, c in enumerate(S)}
        ans = []
        maxPart = 0
        st = 0
        for i, c in enumerate(S):
            maxPart = max(maxPart, lastInd[c])

            if i == maxPart:
                ans.append(len(S[st:i + 1]))
                st = i + 1
        return ans
