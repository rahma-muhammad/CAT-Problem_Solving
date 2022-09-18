class Solution:
    def rotate(self, arr, k): # Rotate the 1D array
        n = len(arr)
        k = k % n  # The array return to its normal order after n times rotations , % tells how much left for the normal
        arr[:] = arr[n - k:] + arr[:n - k]

    def shiftGrid(self, grid, k):
        n , m = len(grid) , len(grid[0])
        #flatten the matrix
        res = []
        for i in range(n):
            for j in range(m):
                res.append(grid[i][j])
        #Rotate
        self.rotate(res, k)
        #Return back to matrix
        for i in range(n):
            for j in range(m):
                grid[i][j] = res[i*m+j]

        return grid

test1 = Solution() # output [[9,1,2],[3,4,5],[6,7,8]]
print(test1.shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
