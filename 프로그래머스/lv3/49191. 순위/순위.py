from collections import deque

def init(n,results):
    graph = [[0]*(n+1) for _ in range(n+1)]
    for a,b in results:
        graph[a][b] = 1
    return graph

def bfs(graph,start,n):
    q = deque([start])
    visited = [0]*(n+1)
    
    while q:
        cur = q.popleft()
        
        for i in range(n+1):
            if graph[cur][i] and not visited[i]:
                q.append(i)
                visited[i] = 1
    return visited

def check(matrix,i,n):
    temp = sum(matrix[i])
    
    for j in range(n+1):
        temp += matrix[j][i]
    return temp==n-1
        
def solution(n, results):
    answer = 0
    graph = init(n,results)
    total = [[0]*(n+1)]
    for i in range(1,n+1):
        total.append(bfs(graph,i,n))
    
    for i in range(1,n+1):
        answer += check(total,i,n)
    return answer

"""
0: [x,x,x,x,x,x]
1: [x,x,o,x,x,o]
2: [x,x,x,x,x,o]
3: [x,x,o,x,x,o]
4: [x,x,o,x,x,o]
5: [x,x,x,x,x,x]

"""