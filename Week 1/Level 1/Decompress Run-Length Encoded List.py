class Solution:
    def decompressRLElist(self, nums):
        res = []
        l= len(nums)
        for i in range(1,l,2):
            res.extend([nums[i] for x in range(nums[i-1])])

        return res

t = Solution()
print(t.decompressRLElist([1,2,3,4]))    # Output: [2,4,4,4]