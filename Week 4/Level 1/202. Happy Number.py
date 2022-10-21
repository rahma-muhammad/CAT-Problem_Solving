from cmath import sqrt
import re


class Solution:
    def square(self, n):
        sum = 0
        while n > 0:
            sum += pow(n%10,2)
            n //= 10
        return sum


    def isHappy(self, n: int) -> bool:
        sum = n
        for i in range(1000):
            sum = self.square(sum)
            if sum == 1:
                return True
        return False

t = Solution()
print(t.isHappy(19)) # True
print(t.isHappy(2)) # False