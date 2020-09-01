# code
def getBitDiffInefficient(arr, N):
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += (bin((arr[i] ^ arr[j])).count("1"))
    return (2 * ans)


def getBitDiffEfficient(arr, N):
    ans = 0
    for i in range(32):
        setbits = 0
        for num in arr:
            # check if ith bit set
            # print(num)
            if (num & (1 << i)):
                setbits += 1
        ans += ((setbits) * (N - setbits))
    return ans * 2


T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().strip().split()))
    # print(getBitDiffInefficient(arr, N))
    print(getBitDiffEfficient(arr, N))
