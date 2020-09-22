"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        if not nums:
            return []
        # only 2 majority elements can be present
        m1 = -1
        m2 = -1

        cnt1 = 0
        cnt2 = 0


        for num in nums:
            if m1 == num:
                cnt1+=1
            elif m2 == num:
                cnt2+=1

            elif cnt1==0:
                cnt1+=1
                m1 = num
            elif cnt2==0:
                cnt2+=1
                m2 = num
            else:
                cnt1-=1
                cnt2-=1
        print(m1 ,m2)
        if m1==m2:
            return [m1]

        ans = []
        cnt1 = 0
        cnt2 = 0

        for m in (m1, m2):
            if nums.count(m) > len(nums)/3:
                ans.append(m)

        # ans.sort()
        return ans
