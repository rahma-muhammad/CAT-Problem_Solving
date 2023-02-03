from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        n = len(intervals)
        intervals = sorted(intervals, key = lambda x : x[1])
        i = 1
        while(i < n):
            if intervals[i][0] < intervals[i-1][1]:
                res += 1
                intervals[i].pop(1)
                intervals[i].pop(0)
                intervals.remove([])
                i -= 1
                n -= 1
            i += 1
        return res

t = Solution()
print(t.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])) #1
print(t.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]])) # 7

