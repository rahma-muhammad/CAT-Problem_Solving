from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i = 1
        list = []
        while i<=n:
            if i % 15 ==0:
                list.append("FizzBuzz")
            elif i % 3 ==0:
                list.append("Fizz")
            elif i% 5 ==0:
                list.append("Buzz")
            else:
                list.append(f"{i}")
            i+=1
        return list

t = Solution()
print(t.fizzBuzz(3)) #["1","2","Fizz"]