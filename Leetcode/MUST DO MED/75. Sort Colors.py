def partition(low, high):
    pivot = low
    i = low+1
    j = high
    while i<=j:
        #move i forward unltil number greater than pivot
        while i<=j and nums[pivot] > nums[i]:
            i+=1
        while  i<=j and nums[pivot] <= nums[j]:
            j-=1
        if i<=j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[pivot], nums[j] = nums[j], nums[pivot]
    return j
def qsort(low, high):
    if low >=high:
        return

    part = partition(low, high)
    # sort left
    qsort(low, part-1)
    qsort(part+1, high)
nums = [0,1]
qsort(0, len(nums)-1)
print(nums)