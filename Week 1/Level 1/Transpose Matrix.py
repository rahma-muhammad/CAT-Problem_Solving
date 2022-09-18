class Solution:
    def transpose(self, matrix) :
        n ,m = len(matrix) , len(matrix[0])
        tran = [[None]*n for k in range(m)]
        for i in range(n):
            for j in range(m):
                tran[j][i] = matrix[i][j]

        return tran

t = Solution()
print(t.transpose([[1,2,3],[4,5,6],[7,8,9]]))  #Output: [[1,4,7],[2,5,8],[3,6,9]]