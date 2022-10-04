from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = []
        for i in nums:
            arr = [j for j in nums if j < i]
            freq.append(len(arr))

        return freq

t =Solution()
print(t.smallerNumbersThanCurrent([8,1,2,2,3])) #Output: [4,0,1,1,3]