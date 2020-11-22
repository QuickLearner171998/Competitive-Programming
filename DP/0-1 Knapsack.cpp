# include <iostream>
using namespace std;

int knapsack(int wt[], int val[], int n, int W){
    int dp[n + 1][W + 1];

    for (int i=0; i <= n; i++){
        for (int weight=0; weight <= W;  weight++){
            if (i == 0 || weight == 0){
                dp[i][weight] = 0;
            }
            else if (weight >= wt[i - 1]){
                dp[i][weight] = max(val[i - 1] + dp[i - 1][weight - wt[i - 1]], dp[i - 1][weight]);
            }
            else if (weight < wt[i - 1]){
                dp[i][weight] = dp[i - 1][weight];
            }
        }
    }
    return dp[n][W];
}

