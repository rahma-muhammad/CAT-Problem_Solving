import sys
class Solution:
    def solveFrog(self, n, arr):
        dp = [sys.maxsize] * n
        dp[0] = 0
        for i in range(n):
            for j in range(i+1,i+k+1):
                if j < n:
                    currDpJ = dp[j]
                    currDpI = dp[i]
                    currAbs = abs(arr[i]-arr[j])
                    whole = dp[i] + abs(arr[i]-arr[j])
                    dp[j] = min(dp[j], dp[i] + abs(arr[i]-arr[j]))
        return dp[n-1]

S = Solution()
n , k= map(int, (input().split()))
arr = list(map(int, input().split(' ')))
print(S.solveFrog(n, arr))

# S = Solution()
#print(S.solveFrog(4, [10, 30, 40, 20]))
#print(S.solveFrog(2, [10, 10]))
#print(S.solveFrog(6, [30, 10, 60, 10, 60, 50]))