import sys
from collections import deque

r,c = map(int,input().split())
graph = [['.']*c for _ in range(r)]
x,y = 0,0
rain_list = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[False]*c for _ in range(r)]
answer = 'FAIL'
for i in range(r):
    temp = input()
    for j in range(c):
        graph[i][j] = temp[j]
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'W':
            x,y = i,j
        if graph[i][j] == '*':
            rain_list.append((i,j))
q = deque([])
for i in range(len(rain_list)):
    q.append((rain_list[i][0],rain_list[i][1],0,'*'))
q.append((x,y,0,'W'))
visited[x][y] = True
while q:
    x,y,count,who = q.popleft()
    if who == '*':
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<r and 0<=ny<c and graph[nx][ny] == '.':
                graph[nx][ny] = '*'
                q.append((nx,ny,0,'*'))
    else:
        if graph[x][y] == 'H':
            answer = count
            break

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and (graph[nx][ny] == '.' or graph[nx][ny] == 'H'):
                q.append((nx,ny,count+1,'W'))
                visited[nx][ny] = True
print(answer)
