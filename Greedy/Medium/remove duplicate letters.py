class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        stack = []
        visited = []
        last_index = {}
        for i in range(n):
            last_index[s[i]] = i

        for i in range(n):
            if s[i] not in visited:
                while (stack and stack[-1] > s[i] and last_index[stack[-1]] > i):
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.append(s[i])

        return ''.join(stack)

t = Solution()
print(t.removeDuplicateLetters('bcabc'))
print(t.removeDuplicateLetters("cbacdcbc"))  #acdb