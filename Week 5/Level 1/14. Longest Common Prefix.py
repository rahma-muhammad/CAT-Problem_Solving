from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        res = strs[0]
        for word in strs[1:]:
            while word.find(res) != 0:
                res = res[0:len(res)-1] #if 
                if len(res)==0:
                    return ""
        return res


t = Solution()
print(t.longestCommonPrefix(["flower","flow","flight"])) #fl
print(t.longestCommonPrefix(["dog","racecar","car"])) #''
print(t.longestCommonPrefix('a'))
print(t.longestCommonPrefix(["flower","flower","flower","flower"]))
print(t.longestCommonPrefix(['c', 'ac', 'ccc']))