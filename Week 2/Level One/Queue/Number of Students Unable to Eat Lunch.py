from collections import deque
from re import S
from typing import List
import math
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while sandwiches and students and sandwiches[0] in students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
                

        return len(students)
        
t = Solution()
print(t.countStudents( [1,1,0,0], [0,1,0,1])) # 0
print(t.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1])) # 3
