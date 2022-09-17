class Solution:
    def maximumWealth(self, accounts) -> int:
        maxs = [] # To hold the amount of money for each person
        for i in range(len(accounts)):
            temp = 0
            for j in range(len(accounts[i])):
                temp += accounts[i][j]
            maxs.append(temp)
        return max(maxs)

test = Solution()
print(test.maximumWealth([[1,2,3],[3,2,1]])) # should be 6

test2 = Solution()
print(test2.maximumWealth([[1,5],[7,3],[3,5]])) # should be 10