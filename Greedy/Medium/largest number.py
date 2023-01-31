from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(map(bool, nums)):
            return '0'
        start , end = 0 , 1
        n = len(nums)
        strs = [str(i) for i in nums]
        while (start < n and end < n):
            first = strs[start] + strs[end]
            second = strs[end] + strs[start]
            if first < second :
                temp = strs[start] 
                strs[start] = strs[end]
                strs[end] = temp
            if end == n - 1:
                start += 1
                end = start + 1
            else:
                end += 1
        
        return ''.join(strs)

t = Solution()
print(t.largestNumber([10, 2])) #210
print(t.largestNumber([3,30,34,5,9])) #9534330
print(t.largestNumber([1])) #1
print(t.largestNumber([0, 0])) #0