from subprocess import list2cmdline
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = list("qwertyuiop")
        second = list("asdfghjkl")
        third = list("zxcvbnm")
        specified = []
        res = []
        for word in words:
            if word[0].lower() in first:
                specified = first
            elif word[0].lower() in second:
                specified = second
            elif word[0].lower() in third:
                specified = third
            for letter in word:
                if letter.lower() not in specified:
                    break
            else:
                res.append(word)
        return res

t =Solution()
print(t.findWords(["Hello","Alaska","Dad","Peace"])) #Alaska, Dad