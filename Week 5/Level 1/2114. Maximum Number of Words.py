from ast import Str
from typing import List


class Solution:
    def countwords(self, sentence: Str):
        count = 0
        for letter in sentence:
            if letter == ' ':
                count+=1
        return count+1


    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        for sentence in sentences:
            if self.countwords(sentence) > max:
                max = self.countwords(sentence)

        return max

t = Solution()
print(t.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))