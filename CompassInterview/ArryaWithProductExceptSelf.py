"""Given an input array of integers, return an array of the 
same size such that nth element in the output array is the 
product of every element in the input array other than the nth
element of the input array. Restriction: do not use division in your algorithm. This should be done in O(n) time complexity.

Input:  [1,2,3,4]
Output: [24,12,8,6]

"""

# maintain Lefte and right products

# Left Product
arr = [1,2,3,4]
ans = [1]*len(arr)
lp = arr[0]

for i in range(1, len(arr)):
	ans[i] = lp
	lp=lp*arr[i]

# Right product
rp = arr[-1]
for i in range(len(arr)-2, -1, -1):
    ans[i] = ans[i]*rp
    rp = rp*arr[i]

print(ans)

	