class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        arr = []
        l = len(bin(max(num1, num2))[2:])
        for num in range(0, pow(2, l)):
            if bin(num).count('1') == bin(num2).count('1'):
                arr.append(num)

        min = arr[0]
        res= min ^ num1
        for a in arr[1:]:
            if a ^ num1 < res:
                min = a
                res = a ^ num1

        return min

s = Solution()
print(s.minimizeXor(79, 74)) #76 #Time Limit Exceeded