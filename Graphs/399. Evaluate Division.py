"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def makeGraph(eqns, vals):
            g = {}
            for eqn, val in zip(eqns, vals):
                if eqn[0] in g:
                    g[eqn[0]].append((eqn[1], val))
                else:
                    g[eqn[0]] = [(eqn[1], val)]
                if eqn[1] in g:
                    g[eqn[1]].append((eqn[0], 1/val))
                else:
                    g[eqn[1]] = [(eqn[0], 1/val)]
                    
            return g
        
        def doBFS(g, src, tgt):
            q = []
            mult = {node:1.0 for node in g}
            visited = {node:0 for node in g}
            mult[src] = 1.0
            q.append((src,1.0))
            visited[src] = 1
            
            while q:
                node, wt = q.pop(0)
                if node == tgt:
                    return mult[tgt]
                for nbr in g[node]:
                    nd, val = nbr
                    if not visited[nd]:
                        visited[nd] = 1
                        mult[nd] = mult[node] * val
                        q.append((nd, val))
            if visited[tgt]!=1:
                return -1.0
            return mult[tgt]
                
                
        g = makeGraph(equations, values)
        # print(g)
        ans = []
        for query in queries:
            if query[0] not in g or query[1] not in g:
                ans.append(-1.0)
                continue
            ans.append(doBFS(g, query[0], query[1]))
        return ans
        