def isPalindrome(x):

    if x < 0:
        return False
    if x // 10 == 0:
        return True
    import math
    n = int(math.log10(x) + 1)
    digits = [0] * n
    for i in range(n - 1, -1, -1):
        digits[i] = x % 10
        x //= 10
    i = 0
    j = len(digits) - 1
    while(i < j):
        if digits[i] != digits[j]:
            return False
        i += 1
        j -= 1
    return True


def partitionString(s, st, ans):
    for i in range(st, len(s)):
        ss = s[st:i]
        if isPalindrome(ss):
            ans.append(ss)
            partitionString(s, st + 1, ans)


def pallindromicPartions(s):


print(pallindromicPartions("nitin"))
