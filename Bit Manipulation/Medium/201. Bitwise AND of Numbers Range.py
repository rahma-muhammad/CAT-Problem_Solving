class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0
        while right > 0 and left > 0:
            msb1 = len(bin(left)[2:]) - 1
            msb2 = len(bin(right)[2:]) - 1
            if msb1 != msb2:
                break
            else:
                val = pow(2, msb1)
                res += val
                right -= val
                left -= val

        return res


t = Solution()
print(t.rangeBitwiseAnd(0,1))