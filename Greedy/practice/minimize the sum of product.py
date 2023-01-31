class Solution:
    def minValue(self, a, b, n):
        # Your code goes here
        a = sorted(a)
        b = sorted(b, reverse=True)
        sum = 0
        for i in range(n):
            sum += a[i] * b[i]

        return sum

t = Solution()
print(t.minValue([3, 1, 1],[6, 5, 4], 3)) #23
print(t.minValue([6, 1, 9, 5, 4],[3, 4, 8, 2, 4], 5)) #80