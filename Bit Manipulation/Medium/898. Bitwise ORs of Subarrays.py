from typing import List
from collections import Counter

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        my_set = set(arr)
        prev = set()
        prev.add(arr[0])
        for num in arr[1:]:
            temp = set()
            for p in prev:
                temp.add(num | p) #keep track of previous oring of each num
                my_set.add(num | p)
            prev = temp
            prev.add(num)

        return len(my_set)         

t = Solution()
print(t.subarrayBitwiseORs([1,2,4]))