"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"

"""
from functools import cmp_to_key


class Solution:
    '''
    Eg- ['30', '3', '320']
    Sorting methodology -> x = "30" , y = "3"
    x+y = "303" and y+x = "330"
    y+x is greater this implies y is greater. Therefore, y comes before x.

    ans => ['3', '320', '30']
    '''
    @staticmethod
    def compare(a, b):
        if a + b > b + a:
            return -1
        else:
            if a + b < b + a:
                return 1
            return 0

    def largestNumber(self, nums: List[int]) -> str:

        a = "".join(sorted(map(str, nums), key=cmp_to_key(self.compare)))

        # Converting it to int to avoid trailing zeros i.e if a = "000" then it should be "0"
        return str(int(a))
