class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []

        def dfs(depth, cur, start):
            nonlocal output
            if n - sum(cur) < sum([i for i in range(start, start + depth)]):
                return
            if depth == 1 and start <= n - sum(cur) < 10:
                output.append(cur + [n - sum(cur)])
                return
            for i in range(start, 10):
                dfs(depth - 1, cur + [i], i + 1)

        dfs(k, [], 1)
        return output
