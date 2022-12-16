def binSort(A, N): 
        #Your code here
        ones = sum(A)
        A[:N-ones] = [0] * (N-ones)
        A[N-ones:] = [1] * ones 
        return A

print(binSort([1, 0, 1, 1, 0], 5)) # 0, 0, 1, 1, 1