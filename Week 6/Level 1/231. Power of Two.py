class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        powerdict = {}
        for i in range(0, 32):
            powerdict[(2 ** i)] = i

        if n in powerdict:
            return True
        else:
            return False


t = Solution()
print(t.isPowerOfTwo(8))