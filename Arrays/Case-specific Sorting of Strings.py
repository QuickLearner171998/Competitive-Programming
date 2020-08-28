"""Given a string S consisting of uppercase and lowercase characters. The task is to sort uppercase and lowercase letters separately such that if the ith place in the original string had an Uppercase character then it should not have a lowercase character after being sorted and vice versa.

Example 1:

Input:
N = 12
S = defRTSersUXI
Output: deeIRSfrsTUX
Explanation: Sorted form of given string
with the same case of character as that
in original string is deeIRSfrsTUX
Example 2:

Input:
N = 6
S = srbDKi
Output: birDKs
Explanation: Sorted form of given string
with the same case of character will
result in output as birDKs.
Your Task:
You only need to complete the function caseSort that returns sorted string.

Expected Time Complexity: O(N*Log(N)).
Expected Auxiliary Space: O(N).
"""
#User function Template for python3
'''
    Your task is to return the case sorted string
    as described in the problem statement above.

    Function Arguments: string s and size n.
    Return Type: string
'''
def caseSort(s,n):
    #code here
    lower = ""
    upper = ""

    for ch in s:
        if ch.isupper():
            upper+=ch
        else:
            lower+=ch

    upper = ''.join(sorted(upper))
    lower = ''.join(sorted(lower))

    lp = 0
    up = 0
    ans = ""

    for i in range(n):
        if up < len(upper) and s[i].isupper():
            ans+=upper[up]
            up+=1
        elif lp < len(lower) and s[i].islower():
            ans+=lower[lp]
            lp+=1
    return ans


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(caseSort(s,n))
# } Driver Code Ends
