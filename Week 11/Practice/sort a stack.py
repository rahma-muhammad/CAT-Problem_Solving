class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        # Code here
        if len(s) != 0:
            temp = s.pop()
            self.sorted(s)
            self.insertSorted(s, temp)
    
    def insertSorted(self, s, element):
        if len(s) == 0 or element > s[-1]:
            s.append(element)
        else:
            temp = s.pop()
            self.insertSorted(s, element)
            s.append(temp)
        
        
        



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends