class Solution:
    #Complete this function
    def myPow(self, x: float, n: int) -> float:
        f = self.func(x, n)
        return float(f) if n>=0 else (1 / float(f))
    
    def func(self, x, n):
        n =abs(n)
        if n == 0:
            return 1
        elif n % 2 == 0:
            return self.func(x*x, n//2)
        else:
            return x * self.func(x*x, (n-1)//2)
t = Solution()
print(t.myPow(2.00000, 10))#1024.0