from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        pre = [0] * (n+1)
        for i in range(n):
            pre[i+1] = pre[i] + arr[i]


        res = 0
        for i in range(k + 1, n+1):
            maxi = pre[i] - pre[i - k]
            if maxi / k >= threshold:
                res += 1

        return res

s = Solution()
print(s.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4)) #3
print(s.numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5)) #6