"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

#       O(N)
#       https://stackoverflow.com/a/48317895/7519009
        if k<=0 or t<0 or len(nums)==0:
            return 0
        # all elements of any bucket in buckets will have difference <= t
        buckets = {num//(t+1) : [] for num in nums}
        # print(bucket)
        for i, num in enumerate(nums):
            # if bucket not empty then we have at least two elemnts in bucket and their differnce is <=t
            if len(buckets[num//(t+1)]):
                return 1
            # we may have elements with diff <=t in neighbouring buckets ex- if t=3 then 4-2=2 <3
            # also it is ensured that at a time we will have  at most one element in bucket
            currentBucket = num//(t+1)
            buckets[currentBucket].append(num)
            if currentBucket - 1 in buckets and len(buckets[currentBucket - 1]) and num - buckets[currentBucket - 1][0]<=t:
                return 1
            if currentBucket + 1 in buckets and len(buckets[currentBucket + 1]) and buckets[currentBucket + 1][0] - num <=t:
                return 1


            if i>=k:

                # if we move to next window reinit the first elemnt bucket from buckets
                buckets[nums[i-k]//(t+1)] = []

        return 0


#         O(n^2)
#         if k<=0 or t<0 or len(nums)==0:
#             return 0
#         withIndex = []
#         for i, num in enumerate(nums):
# #             (val,ind)
#             withIndex.append((num, i))
#         withIndex.sort(key = lambda x:x[0])
#         for i in range(len(withIndex)):
#             for nexti in range(i+1, len(withIndex)):

#                 if withIndex[nexti][0] - withIndex[i][0]<=t and abs(withIndex[nexti][1] - withIndex[i][1])<=k:
#                     return 1
#                 if withIndex[nexti][0] - withIndex[i][0] > t:
#                     break
        # return 0
