#User function Template for python3
class Solution:
	
    def findMaxSum(self,arr, n):
        temp = [0] * n
        temp[0] = arr[0]
        temp[1] = max(arr[0], arr[1])
        for i in range(2, n):
            temp[i] = max(temp[i-1], arr[i] + temp[i-2])
        
        return temp[-1]

t = Solution()
print(t.findMaxSum([5, 5, 10, 100, 10, 5], 6)) #110
print(t.findMaxSum([3, 2, 7, 10], 4)) #13