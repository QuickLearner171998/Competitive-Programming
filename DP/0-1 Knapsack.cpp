# include <iostream>
using namespace std

int knapsack(int wt[], int val[], int n, int W){
    int dp[n + 1][W + 1]

    for (int i=0
         i <= n
         i + +){
        for (int weight=0
             weight <= W
             weight + +){
            if (i == 0 | | weight == 0){
                dp[i][weight] = 0
            }
            else if (weight >= wt[i - 1]){
                dp[i][weight] = max(val[i - 1] + dp[i - 1][weight - wt[i - 1]], dp[i - 1][weight])
            }
            else if (weight < wt[i - 1]){
                dp[i][weight] = dp[i - 1][weight]
            }
        }
    }
    return dp[n][W]
}

int main()
{
    int t
    cin >> t
    while(t - -)
    {
        int W, n, i
        cin >> n
        cin >> W
        int wt[n]
        int val[n]

        for(i=0
            i < n
            i + +){
            cin >> val[i]
        }

        for(i=0
            i < n
            i + +){
            cin >> wt[i]
        }

        cout << knapsack(wt, val, n, W) << "\n"
    }
    return 0
}
