import heapq as h
from collections import defaultdict
INF = int(1e9)

def dijkstra(graph,start,V):
    heap = []
    distance = [INF]*(V+1)
    distance[start] = 0
    h.heappush(heap,(distance[start],start))

    while heap:
        cur_dist, cur_node = h.heappop(heap)
        for next_dist,next_node in graph[cur_node]:
            if distance[next_node] > cur_dist + next_dist:
                distance[next_node] = cur_dist + next_dist
                h.heappush(heap,(distance[next_node],next_node))
    
    return distance

if __name__ == '__main__':
    V,E = map(int,input().split())
    K = int(input())
    graph = defaultdict(list)

    for _ in range(E):
        u,v,w = map(int,input().split())
        graph[u].append((w,v))

    for answer in dijkstra(graph,K,V)[1:]:
        if answer == INF:
            print('INF')
        else:
            print(answer)