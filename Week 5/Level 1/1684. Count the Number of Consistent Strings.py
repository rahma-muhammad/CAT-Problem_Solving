from typing import List


class Solution:
    def isconsist(self, allowed ,word):
        for letter in word:
            if letter not in allowed:
                return 0
        return 1

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        num = 0
        for word in words:
            num += self.isconsist(allowed, word)

        return num

t = Solution()
print(t.countConsistentStrings( "ab", ["ad","bd","aaab","baa","badab"])) #2