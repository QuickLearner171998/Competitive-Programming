class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        def insertionSort(nums):
            #ins sort
            
            # in each iter left of array should be sorted and right unsorted

            for i in range(1, len(nums)):
                j = i-1
                curr = nums[i]
                while j>=0 and nums[j] > curr:
                    nums[j+1] = nums[j]
                    j-=1
                nums[j+1] = curr
            return nums

        def selectionSort(nums):
            for i in range(len(nums)):
                mini = pow(10, 5)
                min_ind = i
                for j in range(i, len(nums)):
                    if nums[j] < mini:
                        mini = nums[j]
                        min_ind = j
                nums[i], nums[min_ind] = nums[min_ind], nums[i]
            return nums
        
        
        def bubbleSort(nums):
            for j in range(len(nums)-1):
                no_swaps = 1          
                for i in range(len(nums)-1):
                    if nums[i]>nums[i+1]:
                        nums[i], nums[i+1] = nums[i+1], nums[i]
                        no_swaps = 0
                if no_swaps:
                    break
            return nums

        
        def merge(arr1, arr2):
            l1 = len(arr1)
            l2 = len(arr2)
            
            i, j = 0, 0
            ans = []
            while i<l1 and j<l2:
                if arr1[i]<=arr2[j]:
                    ans.append(arr1[i])
                    i+=1
                else:
                    ans.append(arr2[j])
                    j+=1
                    
            while i<l1:
                ans.append(arr1[i])
                i+=1
            while j<l2:
                ans.append(arr2[j])
                j+=1
            return ans
        
        def mergeSort(nums):
            if len(nums)<=1:
                return nums
            mid = (len(nums)-1)//2
            left = mergeSort(nums[:mid+1])
            right = mergeSort(nums[mid+1:])
            return merge(left, right)
            
            
        def quickSortPart(nums, st, end):
            pivot = st
            i=pivot+1
            j = end
            while i<=j :
                # move i forward untli nums[i] < pivot
                while i<=j and nums[pivot] >= nums[i]:
                    i+=1
                while i<=j and nums[pivot] <= nums[j]:
                    j-=1
                if i<j:
                    nums[i], nums[j] = nums[j], nums[i]
            
            nums[j], nums[pivot] = nums[pivot], nums[j]
            
            return j
                
                
        def quickSort(nums,st, end):
            if st < end:
                part = quickSortPart(nums, st, end)
                quickSort(nums, st, part-1)
                quickSort(nums, part+1, end)
            
        
        # quickSort(nums, 0, len(nums)-1)
        
        return mergeSort(nums)
    
    