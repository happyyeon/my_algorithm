INF = 100000007

if __name__ == '__main__':
	N = int(input())
	dp = [3]*(N+1)
	for i in range(2,N+1):
		dp[i] = (dp[i-1]*2)%INF
	print(dp[N]%INF)
