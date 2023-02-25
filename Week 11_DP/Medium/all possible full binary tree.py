# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
	def allPossibleFBT(self, n: int):
            dp = {}
            def backtrack(n):
                if n == 0:
                    return []
                if n == 1:
                    return [TreeNode()]
                if n in dp:
                    return dp[n]
                res = []
                for l in range(n): # 0 -> n - 1
                    r = n - 1 - l
                    leftTrees, rightTrees = backtrack(l), backtrack(r)

                    for t1 in leftTrees:
                        for t2 in rightTrees:
                            temp = TreeNode(0, t1, t2)
                            res.append(temp)
                dp[n] = res
                return res
            return backtrack(n)
	

S = Solution()
print(S.allPossibleFBT(7))
		