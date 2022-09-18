class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        L = 0
        R = 1
        maxP = 0
        while R < n:
            if prices[L] < prices[R]:
                curr = prices[R] - prices[L]
                maxP = max(maxP, curr)
            else:
                L = R
            R += 1

        return maxP

t = Solution()
print(t.maxProfit([7,1,5,3,6,4]))
