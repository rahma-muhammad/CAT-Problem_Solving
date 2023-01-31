#User function Template for python3

#User function Template for python3

class Solution:
    def SumOfDigits(self, N):
        res = 0
        while (N > 0):
            res += (N % 10)
            N = N // 10
        return res

    def BalancedString(self,N):
        #code here
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        res = [alpha * (N // 26)]
        originalN = N
        N = N % 26
        if N == 0:
            return res[0]
        count = (N // 2) + ((N % 2)*(1 - (self.SumOfDigits(originalN) % 2)))
        res.append(alpha[:count])
        res.append(alpha[26- (N - count):])
        
        return ''.join(res)


t = Solution()
print(t.BalancedString(21)) #abcdefghijpqrstuvwxyz