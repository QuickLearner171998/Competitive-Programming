class Solution:
    
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        if r==0:
            return -1
        
        c = len(grid[0])
        if c==0:
            return -1
        q = []
        totalFresh = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]== 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    totalFresh+=1
                    
        if totalFresh == 0:
            return 0
        time = 0
        while(len(q)):
            
            for i in range(len(q)):
                x, y = q.pop(0)
                
                if x> 0 and grid[x-1][y]==1:
                    grid[x-1][y] = 2
                    totalFresh-=1
                    q.append((x-1, y))
                if x<r-1  and grid[x+1][y]==1:
                    grid[x+1][y] = 2
                    totalFresh-=1
                    q.append((x+1, y))
                if y> 0 and grid[x][y-1]==1:
                    grid[x][y-1] = 2
                    totalFresh-=1
                    q.append((x, y-1))
                if y < c-1 and grid[x][y+1]==1:
                    grid[x][y+1] = 2
                    totalFresh-=1
                    q.append((x, y+1))                    
                    
            if(len(q)):
                time+=1
        if totalFresh:
            return -1
        return time
                    
            