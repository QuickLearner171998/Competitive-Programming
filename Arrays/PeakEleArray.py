class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        st = 0
        en = len(nums)
        while (st <= en):
            mid = (en + st) // 2
            print(mid)
            if(mid > 0 and mid < len(nums) - 1):
                if(nums[mid - 1] <= nums[mid] and nums[mid + 1] <= nums[mid]):
                    return mid
                if nums[mid - 1] > nums[mid]:
                    en = mid
                elif (nums[mid + 1] > nums[mid]):
                    st = mid
            else:
                if nums[0] > nums[1]:
                    return 0
                else:
                    return len(nums) - 1
