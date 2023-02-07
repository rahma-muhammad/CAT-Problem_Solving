class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                currStr = ''
                while stack[-1] != '[':
                    currStr = stack.pop() + currStr
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit() :
                    num = stack.pop() + num
                stack.append(int(num) * currStr)

        return ''.join(stack)

t = Solution()
print(t.decodeString("3[a2[c]]")) #accaccacc