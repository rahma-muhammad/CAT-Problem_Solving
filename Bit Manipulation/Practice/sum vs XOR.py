def sumXor(n):
    # Write your code here
    count = 0
    bi = bin(n)[2:]
    count = bi.count('0')
    if n == 0:
        return 1    
    return pow(2,count)
            

result = sumXor(0)

print(str(result))

    
