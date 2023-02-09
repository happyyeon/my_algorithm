import sys
from collections import deque
input = sys.stdin.readline

def init():
    H,W = map(int,input().split())
    input_matrix = []
    for i in range(H):
        input_matrix.append(list(map(int,input().split())))
    Q = int(input())
    return H,W,input_matrix,Q

def solution(input_matrix,i,j,c):
    q = deque([(i-1,j-1)])
    visited = [[False for _ in range(W)] for _ in range(H)]
    visited[i-1][j-1] = True
    origin = input_matrix[i-1][j-1]
    input_matrix[i-1][j-1] = c
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        x,y = q.popleft()

        for a in range(4):
            nx = x+dx[a]
            ny = y+dy[a]

            if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and input_matrix[nx][ny] == origin:
                q.append((nx,ny))
                visited[nx][ny] = True
                input_matrix[nx][ny] = c

    return input_matrix

if __name__ == '__main__':
    H,W,input_matrix,Q = init()
    for _ in range(Q):
        i,j,c = map(int,input().split())
        input_matrix = solution(input_matrix,i,j,c)
    for i in range(H):
        print(*input_matrix[i])
