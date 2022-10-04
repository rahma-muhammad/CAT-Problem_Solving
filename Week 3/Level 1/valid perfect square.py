class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num == 1:
            return True
        start = 2
        end = num
        while start <= end:
            mid = (start + end) // 2
            sq = mid * mid
            if sq < num:
                start = mid + 1
            elif sq > num:
                end = mid - 1
            else:
                return True

        return False

t = Solution()
print(t.isPerfectSquare(16)) # True
print(t.isPerfectSquare(14)) # False
