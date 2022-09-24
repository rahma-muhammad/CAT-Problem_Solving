from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        freq = Counter(s)
        
        for e in s :
            if freq[e] == 1 :
                return s.index(e)
            
        return -1

t = Solution()
print(t.firstUniqChar('leetcode'))