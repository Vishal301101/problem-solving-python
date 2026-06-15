from typing import List

def findMaxLength(nums: List[int]) -> int:
    longest = 0

    for i in range(len(nums)):
        zeros = 0
        ones = 0

        for j in range(i, len(nums)):
            if nums[j] == 0:
                zeros += 1
            else:
                ones += 1

            if zeros == ones:
                longest = max(longest, j - i + 1)

    return longest

print(findMaxLength([0,1,1,1,1,1,0,0,0]))