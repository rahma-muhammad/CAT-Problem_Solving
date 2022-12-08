from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        c = []
        
        for num in range(0, pow(2, n)):
            d = []
            bi = list(bin(num)[2:].rjust(n,'0'))
            d.append(bi[0])
            for i in range(1, len(bi)):
                d.append(str(int(bi[i-1]) ^ int(bi[i])))
            res = int(''.join(d), 2)
            c.append(res)
        return c

t = Solution()
print(t.grayCode(3))