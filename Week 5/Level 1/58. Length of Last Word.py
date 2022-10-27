class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.split()
        return len(res[-1])

t =Solution()
print(t.lengthOfLastWord("Hello World")) #5