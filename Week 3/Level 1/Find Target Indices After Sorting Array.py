from typing import List

def quicksort(array):
        if len(array) < 2:
            return array
        else:
            pivot= array[0]
            less = [ i for i in array[1:] if i <= pivot]
            greater = [ i for i in array[1:] if i > pivot]
            return quicksort(less) + [pivot] + quicksort(greater)

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arr = quicksort(nums)
        i = 0
        targets = []
        for i in range(len(arr)):
            if arr[i] == target:
                targets.append(i)
           
        return targets

t = Solution()
print(t.targetIndices([1,2,5,2,3], 2)) # out 1, 2
print(t.targetIndices([100,1,100] ,100)) # out 1, 2