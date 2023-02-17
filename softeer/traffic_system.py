"""
input: sign_list
output: len(cross)

sign_list,cycle,cur,appointment --> sign 
before,cur,sign ---BFS--> next 
next --> cross_set --> len(cross_set)
"""

import sys
from collections import deque
input = sys.stdin.readline

N,T = map(int,input().split())
sign_list = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N**2):
    x,y = divmod(i,N)
    sign_list[x][y] = list(map(int,input().split()))


def get_next(sign,bx,by,x,y):
    if sign == 1 and y-by == 1:
        return [(-1,0),(0,1),(1,0)]
    if sign == 2 and x-bx == -1:
        return [(0,-1),(-1,0),(0,1)]
    if sign == 3 and y-by == -1:
        return [(-1,0),(0,-1),(1,0)]
    if sign == 4 and x-bx == 1:
        return [(0,-1),(1,0),(0,1)]
    if sign == 5 and y-by == 1:
        return [(-1,0),(0,1)]
    if sign == 6 and x-bx == -1:
        return [(0,-1),(-1,0)]
    if sign == 7 and y-by == -1:
        return [(0,-1),(1,0)]
    if sign == 8 and x-bx == 1:
        return [(1,0),(0,1)]
    if sign == 9 and y-by == 1:
        return [(0,1),(1,0)]
    if sign == 10 and x-bx == -1:
        return [(-1,0),(0,1)]
    if sign == 11 and y-by == -1:
        return [(-1,0),(0,-1)]
    if sign == 12 and x-bx == 1:
        return [(0,-1),(1,0)]
    return []

# BFS
q = deque([(1,0,0,0,0)]) # bx,by,x,y,cycle
cross = set()
while q:
    bx,by,x,y,cycle = q.popleft()
    if cycle > T:
        continue
    cross.add((x,y))
    sign = sign_list[x][y][cycle%4]
    next_list = get_next(sign,bx,by,x,y)

    if next_list:
        for dx,dy in next_list:
            nx = x+dx
            ny = y+dy

            if 0<=nx<N and 0<=ny<N:
                q.append((x,y,nx,ny,cycle+1))
    

print(len(cross))
