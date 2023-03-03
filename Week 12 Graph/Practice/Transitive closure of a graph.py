#User function Template for python3

class Solution:
    def depthFirst(self, graph, source , dest , visited):
        if source == dest:
            return 1
        if source in visited:
            return 0
        visited.add(source)

        for neighbor in graph[source]:
            if (Solution.depthFirst(self, graph, neighbor, dest, visited)) == 1:
                return 1
        return 0
        


    def TurnToGraph(self, N, graph):
        adj = [[j for j in range(N) if graph[i][j]==1] for i in range(N)]
        return adj
    
    def MakeRransitiveClosure(self, N, graph):
        visited = set()
        res = [[Solution.depthFirst(self, graph, i, j, visited=set()) for j in range(N)] for i in range(N)]
        return res

    def transitiveClosure(self, N, graph):
        # code here
        myList = Solution.TurnToGraph(self, N, graph)
        res = Solution.MakeRransitiveClosure(self, N, myList)
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        graph = []
        for i in range(0,N):
            graph.append([int(j) for j in input().split()])
        ob = Solution()
        ans = ob.transitiveClosure(N, graph)
        for i in range(N):
            for j in range(N):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends