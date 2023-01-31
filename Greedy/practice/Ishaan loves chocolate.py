from typing import List


class Solution:
    def chocolates(self, n : int, arr : List[int]) -> int:
        # code here
        arr = sorted(arr)
        return arr[0]
        
t = Solution()
print(t.chocolates(5, [5, 3, 1, 6, 9])) #1