import collections

class Solution:
    def findLucky(self, arr) -> int:
        freq = collections.Counter(arr)
        maxKey = -1
        for key ,value in freq.items():
            if key == value and key > maxKey:
                maxKey = key

        return maxKey

test1 = Solution()
print(test1.findLucky([2,2,3,4])) #Output : 2

test1 = Solution()
print(test1.findLucky([1,2,2,3,3,3])) # 3

test1 = Solution()
print(test1.findLucky([2,2,2,3,3])) # -1