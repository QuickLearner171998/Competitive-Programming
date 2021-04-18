class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        if len(f)==1:
            if f[0]==0:
                return 1
            else:
                if n==0:
                    return 1
            return 0
            
        i = 1
        if f[0]==0 and f[1]==0:
            n-=1
            f[0] = 1
            i+=1
            
        while i<len(f)-1:
            if f[i]==0 and f[i-1]!=1 and f[i+1]!=1:
                n-=1
                if n<=0:
                    return 1
                f[i] = 1
                i+=2
            else:
                i+=1

        if i< len(f):
            
            if f[i]==0 and f[i-1]==0:
                n-=1
        print(n)
        return n<=0
            
                
                