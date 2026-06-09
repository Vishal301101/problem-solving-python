from typing import List
def sortedSquares(nums: List[int]) -> List[int]:
        squares = []
        for i in range(len(nums)):
            numbers = nums[i] * nums[i] 
            squares.append(numbers)
        return sorted(squares)

sortedSquares([-4,7,6,1,2])

# optimal solution

nums = [-4,-1,0,3,10]
result = sorted(x * x for x in range(len(nums)))
print(result)     
      