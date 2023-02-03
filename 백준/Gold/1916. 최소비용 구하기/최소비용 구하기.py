import sys
import heapq as h
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(start,graph_dict):
    dist_list = [INF]*(n+1)
    dist_list[start] = 0
    heap = []
    h.heappush(heap,(0,start))

    while heap:
        cost,cur = h.heappop(heap)

        if dist_list[cur] < cost:
            continue

        for weight,next in graph_dict[cur]:
            if dist_list[next] > cost+weight:
                dist_list[next] = cost+weight
                h.heappush(heap,(cost+weight,next))
    return dist_list

INF = int(1e9)
graph_dict = defaultdict(list)
n = int(input())
m = int(input())
for i in range(m):
    a,b,cost = map(int,input().split())
    graph_dict[a].append((cost,b))
start,end = map(int,input().split())
dist_list = dijkstra(start,graph_dict)
print(dist_list[end])

