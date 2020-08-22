"""
1558. Minimum Numbers of Function Calls to Make Target Array


Your task is to form an integer array nums from an initial array of zeros arr that is the same size as nums.

Return the minimum number of function calls to make nums from arr.

The answer is guaranteed to fit in a 32-bit signed integer.



Example 1:

Input: nums = [1,5]
Output: 5
Explanation: Increment by 1 (second element): [0, 0] to get [0, 1] (1 operation).
Double all the elements: [0, 1] -> [0, 2] -> [0, 4] (2 operations).
Increment by 1 (both elements)  [0, 4] -> [1, 4] -> [1, 5] (2 operations).
Total of operations: 1 + 2 + 2 = 5.

"""


class Solution:

    def checkAllEven(self, nums):
        for ele in nums:
            if ele % 2:
                return False
        return True

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while (sum(nums)):
            # print(nums)
            if self.checkAllEven(nums):
                nums = [i // 2 for i in nums]
                # print(nums)
                ans += 1
            else:
                for i in range(len(nums)):
                    if nums[i] % 2:
                        nums[i] -= 1
                        ans += 1
        return ans
