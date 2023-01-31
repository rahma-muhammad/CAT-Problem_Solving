from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        s1 = ''.join(map(str, nums1))
        s2 = ''.join(map(str, nums2))
        res = 0
        l = 0
        r = 1
        while l < n:
            s = s1[l:r]
            if s in s2:
                res = max(res, r - l)
                r += 1
            else:
                l += 1
                r = l + 1
            if r > n:
                l += 1

        return res


s = Solution()
print(s.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))  # 3
print(s.findLength([70,39,25,40,7],[52,20,67,5,31])) # 0
