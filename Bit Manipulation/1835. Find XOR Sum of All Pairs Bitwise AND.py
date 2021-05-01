class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        """(a1^a2) & (b1^b2) = (a1&b1) ^ (a1&b2) ^ (a2&b1) ^ (a2&b2)"""
        def list_xor(l):
            x = l[0]
            for ele in l[1:]:
                x = x^ele
            return x
        arr1_xor = list_xor(arr1)
        arr2_xor = list_xor(arr2)
        return arr1_xor & arr2_xor