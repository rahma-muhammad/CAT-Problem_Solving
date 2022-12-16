from typing import List
from sys import maxsize

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = maxsize
        left, total = 0, 0
        n = len(nums)
        for i in range(n):
            total += nums[i]
            while total >= target and left < n:
                res = min(res, i - left + 1)
                total -= nums[left]
                left += 1

        return res if res != maxsize else 0

s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3])) #2