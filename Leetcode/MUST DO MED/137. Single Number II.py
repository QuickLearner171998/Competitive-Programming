class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans =  0

        for i in range(32):
            cnt=0
            for n in nums:
                if n & 1<<i:
                    cnt+=1
            mult=(cnt%3) << i
            ans+=(mult)
        
        if ans &  1<<31==0:
            return ans
        # else take 2's complement
        #NEGATE the num
        for i in range(32):
            ans = ans ^ (1<<i)
        ans+=1
        return -1*ans
        
        
#         count = {cnt:0 for cnt in nums}
#         for ele in nums:
#             count[ele]+=1
#         for ele in nums:
#             if count[ele]!=3:
#                 return ele
    