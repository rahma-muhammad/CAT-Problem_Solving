class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        nums = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
        n1, n2 = 0, 0
        for i in range(len(num1)):
            n1 += nums[num1[i]] * pow(10,(len(num1) -1 - i))

        for i in range(len(num2)):
            n2 += nums[num2[i]] * pow(10 ,(len(num2) -1 - i))

        res = n1 + n2
        return str(res)

t =Solution()
print(t.addStrings('11', '123'))
