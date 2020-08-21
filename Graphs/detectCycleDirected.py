# Your task is to complete this function
# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices


def dfs(currNode, curVisi, compVisi, n, graph):

    # make curVisi[currNode] = 1 this means we visited currentNode and
    # for the current node we have not explored all its neighbours
    curVisi[currNode] = 1

    # Now like in dfs we visit the neighbours of the current Node and if a cycle is detected in any of its neighbours
    # that means return True
    for node in graph[currNode]:
        # if a cycle is present then we will return to the current Node even when it has not been explored completely
        # i.e curVisi[node] == 1 during the dfs hence we return True
        if curVisi[node]:
            return True

        # if current Node has been explored completely i.e the node and its neighbours have been visited
        # compVisi[node]=1 so we skip that node as no cycle was detected
        if compVisi[node]:
            continue

        #  if the node is being visited for the first time we recursively run dfs on it
        if dfs(node, curVisi, compVisi, n, graph):
            return True

    # all neighbours visited make compVisis true
    compVisi[currNode] = 1
    curVisi[currNode] = 0
    return False


def isCyclic(n, graph):
    # Code here
    curVisi = [0] * n
    compVisi = [0] * n

    # Check for cycle at each vertex

    for currNode in range(n):

        # dfs will return true for any vertex that means cycle detected!!
        if dfs(currNode, curVisi, compVisi, n, graph):
            return True
    return False


#{
#  Driver Code Starts


from collections import defaultdict


def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        i += 2


if __name__ == '__main__':
    with open("detectCycleSampleInput.txt", "r") as f:
        t = int(f.readline().rstrip())
        # print("t", t)
        for i in range(t):
            n, e = list(map(int, f.readline().rstrip().split()))
            arr = list(map(int, f.readline().rstrip().split()))
            graph = defaultdict(list)
            creategraph(e, arr, graph)
            if isCyclic(n, graph):
                print(1)
            else:
                print(0)
# } Driver Code Ends
