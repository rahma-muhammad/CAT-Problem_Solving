class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = -1
        for i in range(0, len(s)//2 + 1):
            if s[i] != s[n]:
                return False
            n -= 1
        return True

t = Solution()
print(t.isPalindrome(1000021))