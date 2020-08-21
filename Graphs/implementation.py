class Graph(object):
    def __init__(self, V, directed=True):
        # v - no. of vertices
        self.vertices = V
        self.adjList = {i: [] for i in range(V)}
        self.directed = directed

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        #  if undirected then append
        if not self.directed:
            self.adjList[v].append(u)

    def bfs(self, st):
        ans = []
        q = []
        q.append(st)
        visited = [0] * self.vertices
        visited[st] = 1

        while(len(q)):
            n = q.pop(0)
            ans.append(n)
            for ele in self.adjList[n]:
                if visited[ele] != 1:
                    q.append(ele)
                    visited[ele] = 1
        return ans

    def distFromStartNode(self, st):
        dist = [0] * self.vertices
        parent = [-1] * self.vertices
        visited = [0] * self.vertices

        visited[st] = 1
        q = [st]

        while q:
            n = q.pop(0)

            for ele in self.adjList[n]:
                if visited[ele] != 1:
                    parent[ele] = n
                    dist[ele] = dist[n] + 1
                    visited[ele] = 1
                    q.append(ele)
        return dist, parent

    def shortestDistance(self, n1, n2):
        dist, parent = self.distFromStartNode(1)
        print("ParentList ", parent)
        temp = n2
        print("Shortest Path")
        while(temp != -1):
            print(temp, end=" --> ")
            temp = parent[temp]
        print("st")

        print("sh distance between ", n1, n2)
        return dist[n2] - dist[n1]

    def dfsStack(self, st):
        dfs = []
        visited = [0] * self.vertices

        stk = [st]
        # visited[st] = 1

        while stk:
            node = stk.pop()
            dfs.append(node)
            visited[node] = 1
            for neigh in self.adjList[node]:
                if not visited[neigh]:
                    stk.append(neigh)

        return dfs

    def dfsRecur(self, st, dfs, visited):
        if visited[st] == 1:
            return dfs, visited
        dfs.append(st)
        visited[st] = 1

        for neigh in self.adjList[st]:
            self.dfsRecur(neigh, dfs, visited)

        return dfs, visited

        # driver code
V = 6
g = Graph(V)

g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 0)


print("Adj List")
print(g.adjList)

print("BFS")
print(g.bfs(1))

st = 1
print("Distance from ", st)
print(g.distFromStartNode(st)[0])

n1 = 1
n2 = 3
print(g.shortestDistance(n1, n2))


print("DFS")
print("Using Stack")
print(g.dfsStack(st))
dfs = []
visited = [0] * V

print("using recursion")
print(g.dfsRecur(st, dfs, visited)[0])
