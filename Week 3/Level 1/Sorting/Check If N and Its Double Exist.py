from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return arr
        else:
            pivot=arr[0]
            less = [i for i in arr[1:] if i <= pivot]
            greater = [i for i in arr[1:] if i > pivot]

            return self.checkIfExist(less) + [pivot] + self.checkIfExist(greater)