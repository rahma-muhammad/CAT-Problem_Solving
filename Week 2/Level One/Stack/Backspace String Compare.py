class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ls , lt = [] , []
        for i in s:
            if i == '#':
                if ls:
                    temp = ls.pop()
            else:
                ls.append(i)

        for i in t:
            if i == '#':
                if lt:
                    temp = lt.pop()
            else:
                lt.append(i)

        news = ''.join(ls)
        newt = ''.join(lt)
        if news == newt:
            return True
        else:
            return False

t = Solution()
print(t.backspaceCompare('ab#c', 'ad#c'))
print(t.backspaceCompare("ab##", "c#d#"))


