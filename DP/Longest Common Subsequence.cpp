/*

Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.

Input:
First line of the input contains no of test cases  T,the T test cases follow.
Each test case consist of 2 space separated integers A and B denoting the size of string str1 and str2 respectively
The next two lines contains the 2 string str1 and str2 .

Output:
For each test case print the length of longest  common subsequence of the two strings .

Constraints:
1<=T<=200
1<=size(str1),size(str2)<=100

Example:
Input:
2
6 6
ABCDGH
AEDFHR
3 2
ABC
AC

Output:
3
2

Explanation
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.

LCS of "ABC" and "AC" is "AC" of length 2

*/
#include <iostream>
using namespace std;

int lcs(string s1, string s2, int n1, int n2){
    int dp[n1+1][n2+1];
    for(int i=0;i<=n1;i++){
        for(int j=0;j<=n2;j++){
            if(i==0 || j==0){
                dp[i][j] = 0;
            }
        }
    }

    for(int i=1;i<=n1;i++){
        for(int j=1;j<=n2;j++){
            if(s1.at(i-1) == s2.at(j-1)){
                dp[i][j] = 1 + dp[i-1][j-1];
            }
            else{
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }

    return dp[n1][n2];

}

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
    int n1,n2, i;
    cin>>n1;
    cin>>n2;
    string s1, s2;
    cin >> s1;
    cin >> s2;


    cout<< lcs(s1, s2, n1, n2) <<"\n";
    }
    return 0;
}
