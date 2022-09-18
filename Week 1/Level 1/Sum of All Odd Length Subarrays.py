class Solution:
    def sumOneArray(self, arr):
        sum = 0
        for n in arr:
            sum += n
        return sum

    def sumOddLengthSubarrays(self, arr) -> int:
        l = len(arr) + 1
        sum = 0
        for i  in range(1, l, 2):
            index = 0
            while True:
                if (index + i) == l:
                    break
                sum += self.sumOneArray(arr[index:index+i])
                index += 1

        return sum 

t = Solution()
print(t.sumOddLengthSubarrays([1,4,2,5,3]))
