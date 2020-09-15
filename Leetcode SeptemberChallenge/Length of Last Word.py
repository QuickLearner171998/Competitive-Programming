class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        return len(arr[-1]) if len(arr) else 0
