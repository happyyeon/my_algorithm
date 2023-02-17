"""
#1. BFS
#2. 

maps --BFS--> lever_time
maps --BFS--> end_time
lever_time,end_time --sum--> answer
"""

from collections import deque

def find(maps):
    start,end,lever = (0,0),(0,0),(0,0)
    for i in range(r):
        for j in range(c):
            if maps[i][j] == 'S':
                start = (i,j)
            if maps[i][j] == 'E':
                end = (i,j)
            if maps[i][j] == 'L':
                lever = (i,j)
    return start,end,lever

def bfs(sx,sy,ex,ey,maps): # start(x,y) , end(x,y)
    q = deque([(sx,sy,0)])
    visited = [[False]*c for _ in range(r)]
    visited[sx][sy] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while q:
        x,y,cnt = q.popleft()
        
        if (x,y) == (ex,ey):
            return cnt
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and maps[nx][ny] != 'X':
                q.append((nx,ny,cnt+1))
                visited[nx][ny] = True
    return -int(1e9)
    
def solution(maps):
    global r,c
    answer = 0
    r,c = len(maps), len(maps[0])
    
    for i in range(r):
        maps[i] = list(maps[i])
    start,end,lever = find(maps) # start node
    sx,sy = start
    lx,ly = lever
    ex,ey = end
    answer += bfs(sx,sy,lx,ly,maps)
    answer += bfs(lx,ly,ex,ey,maps)
    if answer < 0:
        return -1
    return answer