class Solution:
    def runningSum(self, nums):
        l = len(nums)
        sums = [0] * (l+1)
        for i in range(l):
            sums[i+1] = nums[i] + sums[i]
            
        return sums[1:]