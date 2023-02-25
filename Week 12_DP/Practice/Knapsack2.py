n ,w = map(int,input().split())
wt =[]; val=[]
wt.append(0);val.append(0)
 
for _ in range(n):
  wi , vi = map(int,input().split())
  wt.append(wi)
  val.append(vi)
  
# dp [n][max_val] = 0 
 
max_val = sum(val)
INF = 10 **10
dp = [[INF for i in range(max_val+1)]for j in range(n+1)]
 
for i in range(n+1):
  dp[i][0]=0
 
for i in range(1,n+1):
    wi = wt[i];vi = val[i]
    for V in range(1,max_val+1):
        if vi<=V:
            dp[i][V] = min(wi+dp[i-1][V-vi] , dp[i-1][V])
        else:
            dp[i][V] = dp[i-1][V]
 
res = 0
 
for i in range(max_val+1):
  if dp[n][i] <= w:
    res = i
    
print(res)