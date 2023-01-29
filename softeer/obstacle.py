import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph,i,j,n):
    cnt = 1
    q = deque([(i,j)])
    graph[i][j] = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny]:
                q.append((nx,ny))
                graph[nx][ny] = 0
                cnt += 1
    return cnt,graph

n = int(input())
graph = [[0]*n for _ in range(n)]
for i in range(n):
    temp = input()
    for j in range(n):
        if int(temp[j]):
            graph[i][j] = 1

block_list = list()
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            cnt, graph = bfs(graph,i,j,n)
            block_list.append(cnt)
block_list = sorted(block_list)

block_num = len(block_list)
print(block_num)
for i in range(block_num):
    one_num = block_list[i]
    print(one_num)
