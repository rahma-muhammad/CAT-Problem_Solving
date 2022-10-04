class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        start = 2
        end = x
        while start <= end:
            mid = (start + end ) // 2
            sq = mid * mid
            if sq < x:
                start = mid + 1
            elif sq > x:
                end = mid - 1
            else:
                return mid
        return end

t = Solution()
print(t.mySqrt(8)) #out 2