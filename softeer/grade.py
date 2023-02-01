import sys
import heapq as h
input = sys.stdin.readline

def score_to_rank(mh):
    rank = [0]*n
    now_rank = 1
    save_rank = 0
    save_sc = 0
    while mh:
        now = h.heappop(mh)
        if now[0] == save_sc:
            rank[now[1]] = save_rank
        else:
            rank[now[1]] = now_rank
            save_rank = now_rank
            save_sc = now[0]
        now_rank += 1
    return rank

n = int(input())
score = []
rank = []
max_heap = []
for i in range(3):
    score.append(list(map(int,input().split())))
score.append([0]*n)
for i in range(n):
    score[-1][i] += score[0][i]+score[1][i]+score[2][i]
for i in range(4):
    temp = []
    for j in range(n):
        h.heappush(temp,(-score[i][j],j))
    max_heap.append(temp)
for i in range(4):
    mh = max_heap[i]
    rank.append(score_to_rank(mh))
for i in range(4):
    print(*rank[i])
