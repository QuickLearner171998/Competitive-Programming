# REF
# https://www.youtube.com/watch?v=HN7ey_-A7o4&ab_channel=CodingBlocks

"""
Implement pow(A, B) % C.

In other words, given A, B and C, find (AB)%C.



Input:

The first line of input consists number of the test cases.

 The following T lines consist of 3 numbers each separated by a space and in the following order:

A B C

'A' being the base number, 'B' the exponent (power to the base number) and 'C' the modular.



Output:

In each separate line print the modular exponent of the given numbers in the test case.


Constraints:

1 ≤ T ≤ 70

1 ≤ A ≤ 10^5

1 ≤ B ≤ 10^5

1 ≤ C ≤ 10^5


Example:

Input:

3
3 2 4
10 9 6
450 768 517

Output:

1
4
34
"""


def fastModuloExp(arr):
    base = arr[0]
    exp = arr[1]
    mod = arr[2]

    ans = 1
    while exp:
        if exp % 2:
            ans = (ans * base) % mod
        base = base * base % mod
        exp = exp >> 1
    return ans


T = int(input())

for _ in range(T):
    # N = int(input())
    arr = list(map(int, input().strip().split()))

    print(fastModuloExp(arr))
