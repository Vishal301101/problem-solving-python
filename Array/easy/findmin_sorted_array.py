from typing import List

def findMin(nums: List):
    left = 0
    right = len(nums) - 1 
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid
    return nums[left]

nums = [8,1,2,4,5,6,7]
print(findMin(nums))