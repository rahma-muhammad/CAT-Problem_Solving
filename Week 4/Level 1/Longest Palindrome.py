class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for c in s:
            if c in count.keys():
                count[c] += 1
            else:
                count[c] = 1
        
        len = 0
        odd = 0
        for v in count.values():
            if v % 2 == 0:
                len += v
            else :
                odd = v
                if odd>=2:
                    len += odd - (odd % 2)
                    odd = odd % 2
            
        return len + (odd==1)

t = Solution()
print(t.longestPalindrome('abccccdd'))
print(t.longestPalindrome('ccc'))
                