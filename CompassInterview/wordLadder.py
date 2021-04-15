"""A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
"""
def makeGraph(wordSet):
    g = {word : [] for word in wordSet}
    for word in wordSet:
        for i in range(len(word)):
            for j in range(ord('a'), ord('z')+1):
                t = chr(j)
                if t!= word[i]:
                    new_word = word[:i] + t + word[i+1:]
                    if new_word in wordSet:
                        g[word].append(new_word)
    return g

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log", "cog"]

# print(makeGraph(set(wordList+[beginWord])))
s = set(wordList+[beginWord])
if endWord not in s:
    print(0)
g = makeGraph(s)
# print(g)
# BFS on the graph
visited = set()
src = beginWord
visited.add(src)
q = [src]
ans = 0
dist = {word: -1 for word in s}
dist[src] = 0

while q:
    currW = q.pop(0)
    if currW == endWord:
        print(dist)
        print( dist[currW]+1)
        break
    for nbr in g[currW]:
        if nbr not in visited:
            visited.add(nbr)
            q.append(nbr)
            dist[nbr] = dist[currW]+1
    
        
    
    
    
        
    
    