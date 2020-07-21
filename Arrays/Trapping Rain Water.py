"""

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

"""


class Solution:
    def trap(self, height: List[int]) -> int:
        larr = []
        rarr = [-1] * len(height)
        lmax = 0
        rmax = 0
        for h in height:
            if len(larr) == 0:
                lmax = height[0]
            else:
                lmax = max(lmax, h)
            larr.append(lmax)

        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                rmax = height[i]
            else:
                rmax = max(height[i], rmax)
            rarr[i] = rmax

        water = 0
        for i in range(len(height)):
            water += min(larr[i], rarr[i]) - height[i]

        return water
