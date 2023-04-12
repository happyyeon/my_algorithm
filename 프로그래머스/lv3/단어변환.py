from collections import deque

def make_visited(words):
    visited = dict()
    for w in words:
        visited[w] = False
    return visited

def check(word0,word1):
    cnt = 0
    for i in range(len(word0)):
        if word0[i] != word1[i]:
            cnt += 1
        if cnt >= 2:
            return False
    return True

def bfs(begin,target,words):
    q = deque([(begin,0)])
    visited = make_visited(words)
    visited[begin] = True
    
    while q:
        cur,cnt = q.popleft()
        if cur == target:
            return cnt
        for w in words:
            if not visited[w] and check(cur,w):
                q.append((w,cnt+1))
                visited[w] = True
    return 0                

def solution(begin, target, words):
    return bfs(begin,target,words)
