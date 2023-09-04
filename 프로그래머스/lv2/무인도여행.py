from collections import deque

def bfs(a,b,visited,n,m,maps):
    q = deque([(a,b)])
    visited[a][b] = True
    cnt = int(maps[a][b])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny].isdigit():
                q.append((nx,ny))
                visited[nx][ny] = True
                cnt += int(maps[nx][ny])
    return cnt,visited
        

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j].isdigit() and not visited[i][j]:
                cnt, visited = bfs(i,j,visited,n,m,maps)
                answer.append(cnt)
    if answer:
        answer.sort()
    else:
        answer = [-1]
    return answer
