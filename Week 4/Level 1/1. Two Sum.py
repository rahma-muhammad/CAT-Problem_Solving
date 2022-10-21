from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i , n in enumerate(nums):
            diff = target - n

            if diff in dict:
                return [dict[diff] , i]
            dict[n] = i

t = Solution()
print(t.twoSum([2, 7, 11, 15], 9))