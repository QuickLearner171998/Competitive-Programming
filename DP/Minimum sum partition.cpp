#include <iostream>
using namespace std;


int minSSdiff(int arr[], int n){

    // min(SUM - 2s1)
    int sum = 0;
    for(int i = 0;i<n;i++){
        sum+=arr[i];
    }
    // Eg if sm = 23 then range of ans --> 1,2,3...23
    // but since we are interested in abs value so 2S1 <= SUM i.e S1 <= SUM//2
    // So range of S1 is 1,2, 3...SUM//2
    int sm = int(sum/2);
    
    // Now we check what all values of S1 are possible from above range.
    // For this we use Subset sum problem.
    // And we calculate the dp table and we are interested in only the last row as size of array is n.
    // Ans will be SUM - 2*max(S1)

    bool dp[n+1][sm+1];
    for(int i = 0;i<=n;i++){
        dp[i][0] = true;
    }
    for(int i = 1;i<=sm;i++){
        dp[0][i] = false;
    }

    for(int i=1; i<=n;i++){
        for(int j=1;j<=sm;j++){
            if (j >= arr[i-1]){
                dp[i][j] = (dp[i-1][j-arr[i-1]] || dp[i-1][j]);
            }
            else{
                dp[i][j] = dp[i-1][j];
            }
        }
    }

    for(int i=sm; i>=0; i--){
        if (dp[n][i]){
            return (sum - 2*i);
        }
    }

    return 0;

}


int main()
{
	int t;
	cin>>t;
	while(t--)
	{
	int n,i;
	cin>>n;
	int arr[n];

	for(i=0;i<n;i++){
	    cin>>arr[i];
	}


	cout<< minSSdiff(arr, n) <<"\n";
	}
	return 0;
}
