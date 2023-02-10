import sys
from bisect import bisect_left
input = sys.stdin.readline

# LIS Algorithm with Binary Search
def lis(lst):
    dp = [lst[0]]

    for i in range(N):
        if lst[i] > dp[-1]:
            dp.append(lst[i])
        else:
            idx = bisect_left(dp,lst[i])
            dp[idx] = lst[i]
    return len(dp)

# Input
N = int(input())
lst = list(map(int,input().split()))

# Output
print(lis(lst))
