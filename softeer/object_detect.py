"""
loc_list--DFS-->area
"""
import sys
input = sys.stdin.readline

def dfs(lx,ly,hx,hy,color,cur):
    global area
    if color == K+1:
        if cur < area:
            area = cur
        return

    for a,b in loc_list[color]:
        x1,y1,x2,y2 = lx,ly,hx,hy 

        if a < x1:
            x1 = a
        if b < y1:
            y1 = b
        if a > x2:
            x2 = a
        if b > y2:
            y2 = b

        temp = (x2-x1)*(y2-y1)
        
        if temp < area:
            dfs(x1,y1,x2,y2,color+1,temp)


N,K = map(int,input().split())
loc_list = [[] for _ in range(K+1)]
for _ in range(N):
    x,y,color = map(int,input().split())
    loc_list[color].append((x,y))
area = int(1e9)
for x,y in loc_list[1]:
    dfs(x,y,x,y,2,0)
print(area)
