#include <iostream>
using namespace std;
#include <bits/stdc++.h>

int numberOfcoins(int coins[], int v, int n){
    int dp[n+1][v+1];
    for (int i=0;i<=n;i++){
        dp[i][0] = 0;
    }
    for (int i=0;i<=v;i++){
        dp[0][i] = INT_MAX-1;
    }

    for (int i=1;i<=n;i++){
        for (int j=1;j<=v;j++){
            if (j>=coins[i-1]){
                dp[i][j] = min(1 + dp[i][j-coins[i-1]], dp[i-1][j]);
            }
            else{
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    // for(int i =0; i<=n;i++){
    //     for(int j=0; j<=v;j++){
    //         cout << dp[i][j] << " ";
    //     }
    //     cout <<"\n";
    // }



    if (dp[n][v]>=INT_MAX-1){
        return -1;
    }
    return dp[n][v];


}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
    int v,n,i;
    cin>>v;
    cin>>n;
    int arr[n];

    for(i=0;i<n;i++){
        cin>>arr[i];
    }



    cout<< numberOfcoins(arr, v, n) <<"\n";
    }
    return 0;
}
