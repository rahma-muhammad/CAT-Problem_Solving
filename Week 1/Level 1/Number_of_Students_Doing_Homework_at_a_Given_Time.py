class Solution:
    def busyStudent(self, startTime, endTime, queryTime) -> int:
        freq = 0
        for i in range(0, len(startTime)):
            if queryTime in range(startTime[i], endTime[i] + 1):
                freq += 1

        return freq

test = Solution()
print(test.busyStudent([1,2,3], [3,2,7], 4))
