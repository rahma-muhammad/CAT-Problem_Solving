class Solution:
    def fib(self, n: int) -> int:
        if n in (0, 1):
            return n
        res = [0] * (n+1)
        res[0] = 0
        res[1] = 1
        for i in range(2, n+1):
            res[i] = res[i-1] + res[i-2]

        return res[-1]

t =Solution()
print(t.fib(3)) #2