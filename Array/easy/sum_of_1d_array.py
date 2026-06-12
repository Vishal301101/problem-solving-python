def runSum(nums):     
    for i in range(1,len(nums)):
        nums[i] += nums[i-1]
    return nums

runSum([1,2,3,4])