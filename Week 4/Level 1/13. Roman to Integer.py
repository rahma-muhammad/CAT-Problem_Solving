class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100 , 'D' : 500, 'M' : 1000}
        result = 0

        freaks = {'IV' : 4, 'IX' : 9 ,'XL' : 40, 'XC' : 90,'CD' : 400 , 'CM' : 900}

        while len(s) > 0:
            if s[0:2] in freaks:
                result += freaks[s[0:2]]
                s = s[2:]
            elif s[0] in romans:
                result += romans[s[0]]
                s = s[1:]
            else :
                s = s[1:]
        return result
