import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
dp[1] = 3
for i in range(2,n+1):
    dp[i] = dp[i-1] + 2**(i-1) 
dot = dp[n]**2
print(dot)
