nums = [4,44,555,614,3,1,15,23]

sortedLst = []

def selectionSort(nums):
    for i in range(len(nums)):
        min = 0
        for a in range(len(nums)):
            if nums[a] < nums[min]:
                min =a

        sortedLst.append(nums.pop(min))
    return sortedLst

print(selectionSort(nums))