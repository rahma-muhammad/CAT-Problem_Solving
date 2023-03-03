from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def DFS(path, u):
            if u == len(graph)-1:
                res.append(path + [u])
            else:
                for v in graph[u]:
                    DFS(path + [u], v)

        DFS([], 0)
        return res
    
S = Solution()
print(S.allPathsSourceTarget([[1,2],[3],[3],[]]))