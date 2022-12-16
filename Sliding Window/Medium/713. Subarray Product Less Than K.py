from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k ==1:
            return 0
        n = len(nums)
        pro = 1
        l = 0
        r = 0
        res = 0
        for i in range(n):
            pro *= nums[i] 
            while pro >= k and l < n:
                pro //= nums[l]
                l += 1
            res += i - l + 1
        return res

s = Solution()
print(s.numSubarrayProductLessThanK([10,5,2,6], 100)) #8
print(s.numSubarrayProductLessThanK([1,2,3], 0)) #0
