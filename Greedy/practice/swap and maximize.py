#User function Template for python3
class Solution:

    def maxSum(self, arr, n):
        # code here
        arr = sorted(arr)
        arr_des = sorted(arr, reverse=True)
        sum = 0
    
        for i in range(n):
            sum += abs(arr[i] - arr_des[i])
        
        return sum

t = Solution()
print(t.maxSum([4, 2, 1 , 8], 4)) #18
print(t.maxSum([10, 12], 2)) #4
print(t.maxSum([35 ,98 ,29 ,43, 68 ,49, 76 ,56, 89 ,99, 50 ,85, 66 ,59, 18, 80, 19, 21 ,62 ,88, 42 ,24], 22))