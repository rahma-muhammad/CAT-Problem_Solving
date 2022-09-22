class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for a in s:
            if a == '(' or a == '[' or a =='{':
                stack.append(a)
            elif stack and a == ')' and stack[-1]=='(':
                stack.pop()
            elif stack and a == ']' and stack[-1]=='[':
                stack.pop()
            elif stack and a == '}' and stack[-1]=='{':
                stack.pop()
            else:
                return False
        return not stack

t = Solution()
print(t.isValid('(){}[]')) # True