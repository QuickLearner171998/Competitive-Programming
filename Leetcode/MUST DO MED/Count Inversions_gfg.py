class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.

    def merge(self, arr1, arr2):
        l1 = len(arr1)
        l2 = len(arr2)
        i, j = 0, 0
        ans = []
        cnt=0
        while i<l1 and j < l2:
            if arr1[i] <= arr2[j]:
                ans.append(arr1[i])
                i+=1
            else:
                ans.append(arr2[j])
                j+=1
                cnt+= l1-i
        while i < l1:
            ans.append(arr1[i])
            i+=1
        while j< l2:
            ans.append(arr2[j])
            j+=1
        return cnt, ans
                
    def mergeSort(self, arr, cnt)     :
        if len(arr)<=1:
            return cnt, arr
        mid = (len(arr)-1 )//2
        cnt, left = self.mergeSort(arr[:mid+1], cnt)
        cnt, right = self.mergeSort(arr[mid+1:], cnt)

        c, arr = self.merge(left, right)
        cnt+=c
        return cnt, arr
        
        
    def inversionCount(self, arr, n):
        # Your Code Here
        if n<=1:
            return 0
        ans, _ = self.mergeSort(arr, 0)
        return ans
        

        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends