from collections import deque,defaultdict

def bfs(graph,tx,ty,K):
	q = deque([(0,0,0,K)])
	visited = defaultdict(set)
	visited[K].add((0,0))
	dx = [1,-1,0,0]
	dy = [0,0,1,-1]
	
	while q:
		x,y,cnt,mp = q.popleft()
		
		if (x,y) == (tx,ty):
			return cnt
		
		for i in range(4):
			nx = x+dx[i]
			ny = y+dy[i]
			
			if 0<=nx<R and 0<=ny<C and (nx,ny) not in visited[mp]:
				if graph[nx][ny] == 1:
					if mp >= 10:
						jx,jy = nx+dx[i], ny+dy[i]
						if 0<=jx<R and 0<=jy<C and graph[jx][jy] == 0:
							q.append((jx,jy,cnt+1,mp-10))
							visited[mp-10].add((jx,jy))
				else:
					q.append((nx,ny,cnt+1,mp))
					visited[mp].add((nx,ny))
	return -1

if __name__ == '__main__':
	R,C,K = map(int,input().split())
	graph = [[0]*C for _ in range(R)]
	for i in range(R):
		tmp = input()
		for j in range(len(tmp)):
			graph[i][j] = int(tmp[j])
	
	print(bfs(graph,R-1,C-1,K))
