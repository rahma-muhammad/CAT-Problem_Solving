class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for a in s:
            if stack and a == stack[-1]:
                stack.pop()
            else:
                stack.append(a)
        res = ''.join(stack)
        return res

t = Solution()
print(t.removeDuplicates("aababaab")) #ba
print(t.removeDuplicates("abbaca")) #ca