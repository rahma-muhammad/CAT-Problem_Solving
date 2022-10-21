from re import T
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for i , n in enumerate(nums):

            if n in dict:
                if abs(i-dict[n]) <= k:
                    return True
            dict[n] = i
        return False

t = Solution()
print(t.containsNearbyDuplicate([1,2,3,1], 3))