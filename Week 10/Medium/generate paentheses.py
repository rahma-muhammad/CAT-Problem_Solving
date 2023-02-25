from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open ,close, currString):
            if len(currString) == 2 * n:
                res.append(currString)
                return
            if open < n:
                backtrack(open + 1, close, currString + '(')
            if close < open:
                backtrack(open, close + 1, currString + ')')

        backtrack(0, 0, '')
        return res

t = Solution()
print(t.generateParenthesis(3))