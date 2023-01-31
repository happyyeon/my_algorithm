import sys
import heapq as h
input = sys.stdin.readline

def greedy_knapsack(w,m_list):
    max_price = 0
    while m_list:
        p,m = h.heappop(m_list)
        p *= -1
        if w >= m:
            max_price += m*p
            w -= m
        else:
            max_price += w*p
            break
    return max_price

w,n = map(int,input().split())
m_list = list()
for _ in range(n):
    m,p = map(int,input().split())
    h.heappush(m_list,(-p,m))
max_price = greedy_knapsack(w,m_list)
print(max_price)
