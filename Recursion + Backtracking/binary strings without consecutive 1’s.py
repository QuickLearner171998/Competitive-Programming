"""Generate all binary strings without consecutive 1’s
Last Updated: 03-06-2020
Given a integer K. Task is Print All binary string of size K (Given number).

Examples:

Input : K = 3
Output : 000 , 001 , 010 , 100 , 101

Input : K  = 4
Output :0000 0001 0010 0100 0101 1000 1001 1010   """

# Fibonacci - https://www.youtube.com/watch?v=a9-NtLIs1Kk
# F(1) = 2
# F(2) = 3
# F(3) = 5...

seen = {}


def generateSsNumber(k):
    if k == 1:
        return 2
    if k == 2:
        return 3

    if k in seen:
        return seen[k]
    seen[k] = generateSsNumber(k - 1) + generateSsNumber(k - 2)
    return seen[k]


#Recursion - TLE
"""
def generateSsUtil(prevStr, ans, k):
    if len(prevStr) == k:
        ans.append(prevStr)
        return ans

    if prevStr[-1] == "0":
        ans = generateSsUtil(prevStr + "0", ans, k)
        ans = generateSsUtil(prevStr + "1", ans, k)
    else:
        ans = generateSsUtil(prevStr + "0", ans, k)
    return ans


def generateSs(k):
    ans = generateSsUtil("0", [], k) + generateSsUtil("1", [], k)
    return ans

"""


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        k = int(input())
        print((generateSsNumber(k)) % 1000000007)
