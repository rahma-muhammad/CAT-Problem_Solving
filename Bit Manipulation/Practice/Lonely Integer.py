def lonelyinteger(a):
    # Write your code here
    res = 0
    for i in a:
        res ^= i  # if integer is repeated, its deleted from result
    return res

result = lonelyinteger([1, 3, 5, 1, 3]) #5

print(result)
     
