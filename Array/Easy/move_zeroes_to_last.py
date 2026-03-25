nums = [5,2,0,-3,0,4,6]
def moveZeroesToLast(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == 0:
               temp = nums[i]
               nums[i] = nums[j]
               nums[j] = temp
    return nums

result = moveZeroesToLast(nums)
print(result)
    
# optimize solution should be o(n). Above solution is o(n^2)

def optimalSolution(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j],nums[i] = nums[i],nums[j]
            j+=1
    return nums

print(optimalSolution(nums))
