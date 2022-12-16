# cook your dish here
def FindPower(arr, n , k):
    change_arr = [1 if arr[i] != arr[i+1] else 0 for i in range(n-1)]
    summ = sum(change_arr[:k])
    res = 0
    res += summ
    for i in range(1, n-k):
        summ += change_arr[k+i-1]
        summ -= change_arr[i-1]
        res += summ
    return res

print(FindPower(['a', 'b', 'c' ,'c', 'c'], 5, 2)) #3
print(FindPower(['a','a', 'b', 'b' ,'c', 'c'], 6, 3)) #4

