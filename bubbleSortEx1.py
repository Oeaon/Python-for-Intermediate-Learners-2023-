nums = [4,44,555,614,3]

def bubbleSort (nums):
   for i in range (len(nums)-1):
      if nums[i] > nums[i+1]:
         nums[i],nums[i+1] = nums[i+1], nums[i]

      print(nums)

bubbleSort(nums)
   