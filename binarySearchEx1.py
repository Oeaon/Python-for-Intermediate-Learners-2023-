nums = [3, 24,17,98,10,39,76,1]

#Linear Search - 0(N)

for i in range(len(nums)):
    if nums[i] == 76:
        print(True)
        break

#Binary Search
nums2 = sorted(nums)
lo = 0
hi = len(nums2) - 1

while (lo<hi):
    mid=(lo + hi)//2
    if 76>nums2[mid]:
        lo = mid + 1
    elif 76 < nums2[mid]:
        hi = mid - 1
    else:
        print(True)
        break