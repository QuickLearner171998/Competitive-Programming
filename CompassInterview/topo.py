"""
Given a series of game results such as xxxx beats yyyy, output the final ranking. 

Example 1:

Input: ["a beats b", "b beats c", "c beats d"]
Output: ["a", "b", "c", "d"]
Example 2:

Input: ["a beats b", "a beats c"]
Output: ["a", "b", "c"] or ["a", "c", "b"]

"""
arr = ["a beats b", "a beats c"]

def makeGraph(arr):
    g = {}
    for s in arr:
        u, v = s.split(' beats ')
        if u in g:
            g[u].append(v)
        else:
            g[u] = [v]
        if v not in g:
            g[v] = []


    return g

g = makeGraph(arr)
ans = []

def topo(g, src, ans):
    visited[src] = 1
    for nbr in g[src]:
        if visited[nbr]==0:    
            ans = topo(g, nbr, ans)
    return [src] + ans


visited = {node : 0 for node in g}
for node in g:
    if not visited[node]:
        ans = topo(g, node, ans)
print(ans)