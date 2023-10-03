nums = [4,44,555,614,3,1,15,23]
def insertionSort(nums):
    for i in range (1, len(nums)):
        index = i
        while index > 0 and nums[index] < nums[index-1]:
            nums[index],nums[index -1 ] = nums[index -1 ], nums[index]

            index-=1
    return nums
print(insertionSort(nums))