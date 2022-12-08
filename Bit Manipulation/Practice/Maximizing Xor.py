def maximizingXor(l, r):
    # Write your code here
    res = 0
    for i in range(l, r+1):
        for j in range(i, r+1):
            if (i^j) > res :
                res = i ^ j
                
    return res
            
            


result = maximizingXor(11, 12)

print(str(result)) #7

   
