"""Nearly Sorted Algorithm
Given an array of n elements, where each element is at most k away from its target position. The task is to print array in sorted form.

Input:
First line consists of T test cases. First line of every test case consists of two integers N and K, denoting number of elements in array and at most k positions away from its target position respectively. Second line of every test case consists of elements of array.

Output:
Single line output to print the sorted array.

Constraints:
1 <= T <= 100
1 <= N <= 100
1 <= K <= N

Example:
Input:
2
3 3
2 1 3
6 3
2 6 3 12 56 8
Output:
1 2 3
2 3 6 8 12 56"""
# code
for _ in range(int(input())):
    n, k = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    import heapq

    heap = arr[:k + 1]
    heapq.heapify(heap)
    ans = []
    for j in range(k + 1, n):
        ans.append(heapq.heappop(heap))
        heapq.heappush(heap, arr[j])
    while len(heap):
        ans.append(heapq.heappop(heap))
    print(*ans)
