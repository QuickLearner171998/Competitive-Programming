/*
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.


Constraints:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

*/

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        long long sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum < S){
            return 0;
        }
        sum+=S;
        // let S1 have all +ve and S2 have all -ve
        // S1 - S2 = Sum and S1 + S2 = S(diff)
        // add two --> S1 = (Sum + S)/2
        // So basically we find count of SS with sum S1


        if(sum%2){
            return 0;
        }
        return subsetSum(nums, int(sum/2));

    }

    int subsetSum(vector<int>& nums, int s) {
        int n = nums.size();
        int dp[n+1][s+1];

        // sum= 0
        // if no 0 in nums then only {} empty ss possible so dp[i][0] = 1
        // if 0 in nums dp[i][0] = pow(2, zeros in ss)
        // eg id arr = {0,0,1}  to make sum 0 --> take 1st zero, take 2nd zero, take both zeros, or take none(empty ss)
        // 4 possibilites ie pow(2, nzeros)
        int nzeros = 0;
        dp[0][0] = 1;
        for(int i =1; i<=n;i++){
            if (nums[i-1]==0){
                nzeros++;
            }
            dp[i][0] = pow(2, nzeros);
        }
        for(int i =1; i<=s;i++){
            dp[0][i] = 0;
        }

        for(int i =1; i<=n;i++){
            for(int j=1; j<=s;j++){
                if(j >= nums[i-1]) {
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j];
                }
                else{
                    dp[i][j] =  dp[i-1][j];
                }
            }
        }
        // for(int i =0; i<=n;i++){
        //     for(int j=0; j<=s;j++){
        //         cout << dp[i][j] << " ";
        //     }
        //     cout <<"\n";
        // }
        return dp[n][s];
    }
};
