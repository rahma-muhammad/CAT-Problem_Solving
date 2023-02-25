n, w = map(int, input().split(' '))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [ [0]*(w) for i in range(n)]

for i in range(n):
    weight = arr[i][0]
    value = arr[i][1]
    for j in range(w):
        currWeight = j + 1
        if i == 0 and currWeight >= weight:
            dp[i][j] = value
            continue
        if currWeight == weight:
            dp[i][j] = max(value, dp[i-1][j])
        elif currWeight > weight:
            dp[i][j] = max(dp[i-1][j], value+ dp[i-1][j-weight])
            
        else:
            dp[i][j] = dp[i-1][j]
res =[]
for i in range(n):
    res.append(dp[i][w-1])
print(max(res))
