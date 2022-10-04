from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3 = []

        for i in arr2:
            while i in arr1: # To keep track even after removing
                arr3.append(i)
                arr1.remove(i)
        return arr3 + sorted(arr1)

t= Solution()
print(t.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6])) #Output: [2,2,2,1,4,3,3,9,6,7,19]