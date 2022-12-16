# cook your dish here
def maximumSub(data, n , k):
    pre = [0] * (n+1)
    for i in range(n):
        pre[i+1] = pre[i] + data[i]

#    print(k,data)
#    print(pre)


    best = 0
    best_left = -1
    best_right = -1
    left = 1
    right = 1

    while True:
        total = pre[right] - pre[left-1]

#        print(left,right,total)

        if total <= k and total > best:
            best_left = left
            best_right = right
            best = total

        if total > k:
            left += 1

        if total <=k:
            right += 1

        if right > n or left>n:
            break

    if best_left == -1:
        print(-1)
    else:
        print ( best_left,best_right, best)
        
        
for _ in range(int(input())):
    n , k = map(int, input().split())
    arr = list(map(int, input().split()))
    maximumSub(arr, n , k)