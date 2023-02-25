n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [ [0]*3 for i in range(n+1)]
#Base case
dp[1][0] = arr[0][0]
dp[1][1] = arr[0][1]
dp[1][2] = arr[0][2]

#BU
for i in range(2, n+1):
    dp[i][0] = arr[i-1][0] + max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = arr[i-1][1] + max(dp[i-1][0], dp[i-1][2])
    dp[i][2] = arr[i-1][2] + max(dp[i-1][0], dp[i-1][1])
   

print(max(dp[n][0], max(dp[n][1], dp[n][2])))