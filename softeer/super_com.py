import sys
input = sys.stdin.readline
INF = int(2e9)
def init():
    n,b = map(int,input().split())
    n_list = list(map(int,input().split()))
    return n,b,n_list

def check(mid):
    cost = 0
    for i in range(N):
        if mid > n_list[i]:
            cost += (mid-n_list[i])**2
    if cost > B:
        return True
    return False

def binary_search():
    start, end = 1, INF
    old_com = 1
    while start < end:
        mid = (start+end)//2
        if check(mid):
            end = mid
        else:
            start = mid+1
            old_com = mid
    return old_com

N,B,n_list = init()
old_com_max = binary_search()
print(old_com_max)
