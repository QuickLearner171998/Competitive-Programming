class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        def make_graph(pre, n):
            g = {i:[] for i in range(n)}
            for p in pre:
                u,v = p
                g[v].append(u)
            return g
        def detect_cycle(g, node):
            visited.add(node)
            rec_stack.add(node)
            
            for neigh in g[node]:
                if neigh in rec_stack:
                    return 1
                if neigh not in visited:
                    if detect_cycle(g, neigh):
                        return 1
            rec_stack.remove(node)
            return 0
        g = make_graph(pre, n)
        print(g)
        rec_stack = set()
        visited = set()
        
        for i in range(n):
            if i not in visited:
                if detect_cycle(g, i):
                    return 0
        return 1