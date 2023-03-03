# User function Template for Python3

class Solution:
    def TurnToGraph(self, N, graph):
        mygraph = [[j for j in range(N) if graph[i][j]==1] for i in range(N)]
        return mygraph

    def eulerPath(self, N, graph):
        # code here
        mygraph = Solution.TurnToGraph(self, N , graph)
        noOfEven , noOfOdd = 0, 0
        for i in range(N):
            if len(mygraph[i]) % 2 == 0:
                noOfEven += 1
            else:
                noOfOdd += 1
        if noOfEven == N or noOfOdd == 2:
            return True
        else:
            return False


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        graph = []
        for i in range(N):
            graph.append(list(map(int, input().strip().split())))
        
        ob = Solution()
        print(ob.eulerPath(N, graph))
# } Driver Code Ends
