from inspect import stack


class Solution:
    def maxDepth(self, s: str) -> int:
        max = 0
        stack=[]
        for c in s:
            if c == '(':
                stack.append(c)
                if len(stack) > max:
                    max = len(stack)
            elif c == ')':
                stack.pop() 

        return max

t = Solution()
print(t.maxDepth("(1+(2*3)+((8)/4))+1")) #3
