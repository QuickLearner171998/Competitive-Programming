"""Given a string of character, find the length of longest proper prefix which is also a proper suffix.
Example:
S = abab
lps is 2 because, ab.. is prefix and ..ab is also a suffix.

Input:
First line is T number of test cases. 1<=T<=100.
Each test case has one line denoting the string of length less than 100000.

Expected time compexity is O(N).

Output:
Print length of longest proper prefix which is also a proper suffix.

Example:
Input:
2
abab
aaaa

Output:
2
3
"""


def getLsp(st):
    lsp = [0] * len(st)
    j = 0
    i = 1

    while i < len(st):
        if st[i] == st[j]:
            lsp[i] = j + 1
            j += 1
            i += 1
        else:
            if j == 0:
                lsp[i] = 0
                i += 1
            else:
                j = lsp[j - 1]
    return (lsp[-1])


for _ in range(int(input())):
    st = input().strip()

    print(getLsp(st))
