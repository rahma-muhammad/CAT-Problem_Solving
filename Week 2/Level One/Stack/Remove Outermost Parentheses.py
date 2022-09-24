import re


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack, res = [], ''
        for a in s:
            if a == '(':
                if not stack:
                    stack.append(a)
                else:
                    stack.append(a)
                    res += a
            else:
                if len(stack) == 1:
                    stack.pop(-1)
                else:
                    res += a
                    stack.pop(-1)

        return res


t = Solution()
print(t.removeOuterParentheses("(()())(())"))  # ()()()
print(t.removeOuterParentheses("((()))"))  # "(())"
