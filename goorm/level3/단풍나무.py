from collections import deque

def bfs(graph,sx,sy,visited):
	q = deque([(sx,sy)])
	dx = [1,-1,0,0]
	dy = [0,0,1,-1]
	visited[sx][sy] = True
	
	while q:
		x,y = q.popleft()
		
		for i in range(4):
			nx = x+dx[i]
			ny = y+dy[i]
			
			if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
				if graph[nx][ny] == 0:
					q.append((nx,ny))
					visited[nx][ny] = True
				else:
					graph[nx][ny] -= 1
					if graph[nx][ny] == 0:
						graph[nx][ny] = -1
	
	return graph,visited

def check(graph):
	for i in range(N):
		for j in range(N):
			if graph[i][j]:
				return True
	return False

def color(graph):
	for i in range(N):
		for j in range(N):
			if graph[i][j] < 0:
				graph[i][j] = 0
	return graph
		
if __name__ == '__main__':
	answer = 0
	N = int(input())
	graph = []
	for _ in range(N):
		graph.append(list(map(int,input().split())))
		
	while check(graph):
		visited = [[False]*N for _ in range(N)]
		for i in range(N):
			for j in range(N):
				if graph[i][j] == 0 and not visited[i][j]:
					graph,visited = bfs(graph,i,j,visited)
		graph = color(graph)
		answer += 1
	print(answer)
