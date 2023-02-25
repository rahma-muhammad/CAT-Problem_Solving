class Solution:
    def solve(self, n, k):
        if(n==1):
            return 0
        return ((self.solve(n-1, k)+k)%n)

    def josephus(self, n, k):
        return self.solve(n, k)+1


t = Solution()
print(t.josephus(8, 2)) #1