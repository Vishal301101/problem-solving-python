from typing import List
def subarraySum(nums: List[int], k: int) -> int:
        # count = 0
        # for i in range(len(nums)):
        #     total = 0
        #     for j in range(i,len(nums)): 
        #         total += nums[j]
        #         if total == k:
        #             count += 1  
        # return count
        count = 0
        prefix = 0
        seen = {0: 1}

        for num in nums:
            prefix += num

            if prefix - k in seen:
                count += seen[prefix - k]

            seen[prefix] = seen.get(prefix, 0) + 1

        return count

subarraySum([1,2,3])