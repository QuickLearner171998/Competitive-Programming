class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # O(Lg(N)) Bin Search
        st, end = 0, len(arr)-1
        while st < end:
            mid = (st+end)//2
            if arr[mid+1] > arr[mid]:
                st = mid+1
            else:
                end = mid
        return st
                

        
        
#         # O(N)
#         for i in range(1, len(arr)-1):
#             if arr[i-1] < arr[i] >arr[i+1]:
#                 return i

        
