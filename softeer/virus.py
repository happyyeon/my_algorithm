import sys
input = sys.stdin.readline
INF = 1000000007
k,p,n = map(int,input().split())
dp = [k]*(n+1)
for i in range(1,n+1):
    dp[i] = (dp[i-1]*p)%INF
print(dp[n]%INF)
