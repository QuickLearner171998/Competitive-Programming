class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.s = nums
        heap = []
        for i in range(min(self.k, len(self.s))):
            heap.append(self.s[i])
        for i in range(self.k, len(self.s)):
            heap.sort()
            # in each iteration add number to heap only if its greater than the minimum.
            if self.s[i] >= heap[0]:
                heap.pop(0)
                heap.append(self.s[i])
        self.heap = heap

    def add(self, val: int) -> int:
        if len(self.heap) <self.k:
            self.heap.append(val)
            self.heap.sort()
            return self.heap[0]
        if val >= self.heap[0]:
            self.heap.pop(0)
            self.heap.append(val)
            self.heap.sort()
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)