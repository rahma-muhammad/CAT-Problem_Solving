class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        while True:
            if n % 2 == 0:
                return n
            else:
                n *= 2

t = Solution()
print(t.smallestEvenMultiple(5)) # 10
print(t.smallestEvenMultiple(6)) # 6