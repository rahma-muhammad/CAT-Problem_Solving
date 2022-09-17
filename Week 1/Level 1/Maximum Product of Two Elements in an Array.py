class Solution:
    def maxProduct(self, nums) -> int:
        res = []
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if i != j:
                    res.append((nums[i]-1)*(nums[j]-1))
        return max(res)

test1 = Solution()
print(test1.maxProduct([3,4,5,2])) # output 12

test2 = Solution()
print(test2.maxProduct([1,5,4,5])) # output 16

