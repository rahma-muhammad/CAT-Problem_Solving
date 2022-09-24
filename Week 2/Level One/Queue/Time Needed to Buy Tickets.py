from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sec = 0
        least = tickets[k]
        for i in range(len(tickets)):
            if i > k and tickets[i] >= least:
                sec += least - 1
            elif i < k and tickets[i] > least:
                sec += least
            else:
                sec += tickets[i]
        return sec

t = Solution()
print(t.timeRequiredToBuy([2,3,2], k = 2)) # 6