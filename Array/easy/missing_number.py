nums = [11,12,14,15]

def missingNumber(nums):
    missingNumbers = nums[0]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j] - nums[i] != 1:
                missingNumbers = nums[i] +1

    return missingNumbers

print(missingNumber(nums))
    

