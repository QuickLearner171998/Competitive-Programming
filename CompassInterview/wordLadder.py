class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
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
        # print(makeGraph(set(wordList+[beginWord])))
        s = set(wordList+[beginWord])
        if endWord not in s:
            return 0
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
                return dist[currW]+1
            for nbr in g[currW]:
                if nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)
                    dist[nbr] = dist[currW]+1
        return 0
            
                
            
            
            
                
            
            