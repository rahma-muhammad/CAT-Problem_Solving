class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        l = len(points)
        seconds = 0
        for i in range(l-1):
            first = points[i]
            second = points[i+1]
            res = [e2 - e1 for e2,e1 in zip(second,first)] #list contain (diff x , diff y)
            seconds += abs(max(res, key=abs)) #just add the max difference between them
        return(seconds)


test1 = Solution()
print(test1.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])) #output 7