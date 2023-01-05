import heapq as h
from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    size_cnt = defaultdict(int)
    max_heap = []
    for t in tangerine:
        size_cnt[t] += 1
    for key in size_cnt:
        h.heappush(max_heap,(-1*size_cnt[key],-1*key))
    while k > 0:
        answer += 1
        k -= -1*h.heappop(max_heap)[0]
    return answer