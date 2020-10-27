"""
Maximum Happiness
Geek has R units of money and goes to a bakery to have some pastries. Every pastry costs him 1 unit of money and there is an infinte supply of N different kinds of pastries.
The ith pastry has some ai and bi value associated with it. When Geek eats the ith pastry for the first time, he gets ai amount of happiness. When he eats the ith pastry for the second time, he gets (ai - bi) amount of happiness and so on. When he eats the ith pastry for the kth time, the amount of happiness he gets is equal to max (0, ai - (k-1)*bi).
Find the maximum amount of happiness Geek can get with the amount of money he has.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains two space separated integer values of N and R. The second line contains N space separated pairs of integer (ie, 2*N integers) denoting the values of ai and bi for each pastry.

Output:
Print a single integer denoting the maximum amount of happiness that Geek can gain with the given amount of money he has.

Your Task:
You don't need to read input or print anything. Your task is to complete the function maxHappiness() which takes the array a[], the array b[], their size N and amount of money R as input parameters and returns the maximum amount of happiness that Geek can get. Since the result can be very large, return the result mod 998244353.

Constrains:
1 <= T <= 100
1 <= |N|, |R| <= 2*106
1 <= ai, bi <= 2*106

Example:
Sample Input:
2
2 3
8 2 7 2
2 10
5 1 10 5

Sample Output:
21
30

Explanation:
Test Case 1:
Geek eats the 0-th pastry and gains happiness 8.
Then he eats the 1-st pastry and gains happiness 7.
Then he eats the 0-th pastry and gains happiness 8-2 = 6.
After this, he exhausts all his money. Hence, the total amount of Happiness = 8 + 7 + 6 = 21.
"""


#User function Template for python3

def maxHappiness(a,b,n,r):
    # code here
    import heapq
    l = []
    heapq.heapify(l)

    for i, happiness in enumerate(a):
        heapq.heappush(l, [-1*happiness, i])
    ans = 0
    # print(l)
    for _ in range(r)    :
        tempH, tempI = heapq.heappop(l)
        # print(tempH, tempI)
        # print(l)

        ans+=  -1* tempH
        heapq.heappush(l, [-1*(max(0, -1*tempH - b[tempI] )), tempI  ])

    return ans





#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,r = ( int(x) for x in input().split() )
        s = input().split()
        a = [ int(s[i]) for i in range( 0 , 2*n , 2 ) ]
        b = [ int(s[i]) for i in range( 1,  2*n , 2 ) ]
        print( maxHappiness(a,b,n,r) )

# } Driver Code Ends
