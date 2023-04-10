import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    tp_table = [0]
    for _ in range(N):
        tp_table.append(list(map(int,input().split())))

    dp = [0]*(N+2)
    for i in range(1,N+2):
        dp[i] = max(dp[i],dp[i-1])
        if i<=N and i+tp_table[i][0] <= N+1:
            dp[i+tp_table[i][0]] = max(dp[i+tp_table[i][0]],dp[i]+tp_table[i][1])
    print(max(dp))
