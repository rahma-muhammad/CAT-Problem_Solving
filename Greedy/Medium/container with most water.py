from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        end = n - 1
        start = 0
        while(start < end):
            max_area = max(max_area ,((end - start )* min(height[end], height[start])))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
                
        return max_area


t = Solution()
print(t.maxArea([1,8,6,2,5,4,8,3,7])) #49
print(t.maxArea([1,2])) #1
print(t.maxArea([1, 1])) #1
print(t.maxArea([2,3,4,5,18,17,6])) #17