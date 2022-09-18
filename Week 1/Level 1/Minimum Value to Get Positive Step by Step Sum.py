class Solution:
    def minStartValue(self, nums) -> int:
        startValue = 1
        l = len(nums)
        
        while True:
            flag = True
            res = startValue
            for i in range(l):
                res += nums[i]
                if res < 1:
                    startValue += 1
                    flag = False
                    break
                    # res = startValue
                    # i = 0
            if flag == True:
                break
        return startValue

test1 = Solution()
print(test1.minStartValue([1,-2,-3])) # output 5