class Solution:
    def calPoints(self, operations) -> int:
        stack = []
        for op in operations:
            if op == '+':
                stack.append(stack[-1]+stack[-2])
            elif op == "C":
                stack.pop(-1)
            elif op == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))

        return sum(stack)


t = Solution()
print(t.calPoints(["5", "2", "C", "D", "+"]))  # 30
print(t.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # 27
print(t.calPoints(["1", "C"]))  # 0
