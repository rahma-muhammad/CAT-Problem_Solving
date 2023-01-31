class Solution:
    def minimumMessages (ob,N):
        # code here 
        return 2 * (N-1)

t = Solution()
print(t.minimumMessages(2)) #2
print(t.minimumMessages(3)) #4

#  - ->
#  A -> B -> C 
#  < - - - - -
