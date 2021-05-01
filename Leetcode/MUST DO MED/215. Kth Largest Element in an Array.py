class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #MIN Heap
        min_heap = []
        for i in range(k):
            min_heap.append(nums[i])
        
        for i in range(k, len(nums)):
            min_heap.sort()
            if nums[i] > min_heap[0]:
                min_heap.pop(0)
                min_heap.append(nums[i])
        min_heap.sort()
        return min_heap[0]