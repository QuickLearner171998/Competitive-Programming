# User function Template for python3


def bfs(g, n, visited, currNode):
    q = [currNode]
    visited[currNode] = 1
    parent = [-1] * n
    # parent = [-1]
    while q:
        node = q.pop(0)
        for neigh in g[node]:
            if neigh != parent[node] and visited[neigh]:
                return 1
            if not visited[neigh]:
                q.append(neigh)
                visited[neigh] = 1
                parent[neigh] = node
    return 0


def isCyclic(g, n):
    '''
    :param g: given adjacency list representation of graph
    :param n: no of nodes in graph
    :return:  boolean (whether a cycle exits or not)
    '''
    # code here
    visited = [0] * n

    for i in range(n):
        if not visited[i] and bfs(g, n, visited, i):
            return 1
    return 0



#{
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys
from collections import defaultdict

# Contributed by : Nagendra Jha

# Graph Class:


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):  # add directed edge from u to v.
        self.graph[u].append(v)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        N, E = map(int, input().strip().split())
        g = Graph(N)
        edges = list(map(int, input().strip().split()))

        for i in range(0, len(edges), 2):
            u, v = edges[i], edges[i + 1]
            g.addEdge(u, v)  # add an undirected edge from u to v
            g.addEdge(v, u)
        print(isCyclic(g.graph, N))
# } Driver Code Ends
