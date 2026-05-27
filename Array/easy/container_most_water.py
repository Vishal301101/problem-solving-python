from typing import List
def maxArea(height: List[int]) -> int:
        left = 0
        res = 0
        right = len(height)-1
        while left < right:
            net = min(height[left],height[right]) * (right-left)
            res = max(res,net)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return res

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))