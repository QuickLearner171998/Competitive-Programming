"""Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""
 

Note:

A.length == 4
0 <= A[i] <= 9
"""
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        if len(A)<4:
            return ""
        if sum(A) == 0:
            return "00:00"
        if min(A) > 2:
            return ""
        
        def isValid(s):
            if (s[0]) > "2" or s[2] > "5":
                return 0
            if s[0] == "2":
                if s[1] >"3":
                    return 0
            return 1
        
        
        smax = "0000"
        def generatePermutations(st, end, smax):
            
            if st == end:
                st = str(A[0])+str(A[1])+str(A[2])+str(A[3])
                if isValid(st):
                    smax = max(smax, st)
                    
                return smax
            for i in range(st, end):
                A[i], A[st] = A[st], A[i]
                # print(arr)
                smax = generatePermutations(st+1, end, smax)
                A[i], A[st] = A[st], A[i]
            return smax
        # print(smax)
        ans = (generatePermutations(0, len(A), smax))
        if ans=="0000":
            return ""
        fans = ans[0] + ans[1] +":" + ans[2] +ans[3] 
        return fans
