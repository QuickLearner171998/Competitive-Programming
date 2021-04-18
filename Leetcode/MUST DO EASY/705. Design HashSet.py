class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # since max calls 10k so create a list of len 10001
        self.l = pow(10, 4)+1
        self.arr = [[] for _ in range(self.l)]
        

    def add(self, key: int) -> None:
        n_key = key%self.l
        if not key in self.arr[n_key]:
            self.arr[n_key].append(key)
        

    def remove(self, key: int) -> None:
        n_key = key%self.l
        if key in self.arr[n_key]:
            self.arr[n_key].remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        n_key = key%self.l
        return key in self.arr[n_key]
            
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)