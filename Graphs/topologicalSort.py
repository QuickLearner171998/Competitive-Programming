# Your task is to complete this function
# Function should return Topologically Sorted List
# Graph(adj) is a defaultict of type List
# n is no of edges

# def dfs(node, adj, stk, visited):
#     if visited[node]:
#         return
#     visited[node] = 1

#     for neigh in adj[node]:
#         if not visited[neigh] :
#             dfs(neigh, adj, stk, visited)

#     stk.append(node)

# def topoSort(n, adj):
#     # Code here
#     topoStack = []
#     visited = [0]*n
#     for i in range(n):
#         if not visited[i]:
#             dfs(i, adj, topoStack, visited)

#     return topoStack[::-1]


def parentCount(adj, pcount):
    for key in adj.keys():
        for node in adj[key]:
            pcount[node]+=1




def topoSort(n, adj):
    topoQ = []
    visited = [0]*n
    pcount = [0]*n
    parentCount(adj, pcount)

    for i in range(len(pcount)):
        if not pcount[i]:
            topoQ.append(i)
    ans = []
    while(topoQ):
        pnode = topoQ.pop(0)
        ans.append(pnode)
        for neigh in adj[pnode]:
            pcount[neigh]-=1
            if pcount[neigh]==0:
                topoQ.append(neigh)
    return ans




#{
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
def creategraph(e, n, arr, graph):
    i = 0
    while i<2*e:
        graph[arr[i]].append(arr[i+1])
        i+=2

def check(graph, N, res):
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

from collections import defaultdict
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, N, arr, graph)
        res = topoSort(N, graph)

        if check(graph, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends
