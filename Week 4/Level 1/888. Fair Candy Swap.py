from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        dict1 = {}
        for i in range(len(bobSizes)):
            dict1[bobSizes[i]] = i
        s1 = sum(aliceSizes)
        s2 = sum(bobSizes)
        mid = (s1+s2) // 2
        for i in range(len(aliceSizes)):
            diff = mid - (s1 - aliceSizes[i])
            if diff in dict1:
                return [aliceSizes[i], bobSizes[dict1[diff]]]
        return []

t = Solution()
print(t.fairCandySwap([1,1], [2,2])) #1,2
print(t.fairCandySwap([1,2], [2,3])) # 1,2
print(t.fairCandySwap([2],[1,3])) # 2,3