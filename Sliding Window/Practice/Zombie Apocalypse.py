# cook your dish here
def Cure(arr, n, k , d):
    dp = [1 if i < d else 0 for i in arr]
    mysum = [0] * (n+1)
    for i in range(n):
        mysum[i+1] = mysum[i] + dp[i]

    res = 0
    l, r = 1, 1
    
    while True:
        total = mysum[r] - mysum[l-1]
        best = r - (l- 1)
#        print(left,right,total)

        if total <= k and best > res:
            res = best

        if total > k:
            l += 1

        if total <=k:
            r += 1

        if r > n or l > n:
            break

    return res
    

for _ in range(int(input())):
    n, k, d = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(Cure(arr, n , k , d))