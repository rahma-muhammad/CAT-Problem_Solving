from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        num = 0
        for d in digits:
            num += d * (10**n)
            n -= 1
        num += 1
        res = []
        while num > 0:
            res.insert(0, num%10)
            num = num // 10
        
        return res
t = Solution()
print(t.plusOne( [1,2,3])) # [1,2,4]
print(t.plusOne([9])) #[1, 0]

                
