def maximumCalories(arr, n , k):
    pre = [0] * (n+1)
    for i in range(1, n + 1):
        pre[i] = pre[i-1] + arr[i - 1]
    maxi = pre[k]
    for i in range(k + 1, n+1):
        maxi = max(maxi, pre[i] - pre[i - k])

    return maxi


n , k = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(maximumCalories(arr, n , k))