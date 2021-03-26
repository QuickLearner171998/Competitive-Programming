"""Minimum Platforms 
Medium Accuracy: 46.78% Submissions: 15348 Points: 4
Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms,

 

Example 1:

Input: N = 6 
arr[] = [0900  0940 0950  1100 1500 1800]
dep[] = [0910 1200 1120 1130 1900 2000]
Output: 3
Explanation: 
Minimum 3 platforms are required to 
safely arrive and depart all trains.
 

Example 2:

Input: N = 3
arr[] = [0900 1100 1235]
dep[] = [1000 1200 1240] 
Output: 1
Explanation: Only 1 platform is required to 
safely manage the arrival and departure 
of all trains. 
"""

#User function Template for python3
def minimumPlatform(n,arr,dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''
    # code here
    arr.sort()
    dep.sort()
    
    platformsNeeded = 1
    maxp = 1
    
    i = 1
    j = 0
    
    while(i<len(arr) and j < len(dep)):
        if arr[i] > dep[j]:
            # train will depart first so now no train on platform 
            # so decrement platformsNeeded
            j+=1
            platformsNeeded-=1
            
        else:
            # train is on platform increment platform
            i+=1
            platformsNeeded+=1
            maxp = max(maxp, platformsNeeded)
    return maxp



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(str,input().strip().split()))
        departure = list(map(str,input().strip().split()))
        print(minimumPlatform(n,arrival,departure))
# } Driver Code Ends