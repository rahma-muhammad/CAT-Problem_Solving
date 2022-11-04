from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        for i in range(left, right+1):
            j = i
            while j > 0:
                if j%10 == 0:
                    break
                elif i % (j%10) != 0:
                    break
                j = j // 10
            if j == 0:
                nums.append(i)
        return nums

t = Solution()
print(t.selfDividingNumbers(1, 22)) #[1,2,3,4,5,6,7,8,9,11,12,15,22]