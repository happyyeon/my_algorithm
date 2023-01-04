import heapq as h

def solution(k, score):
    answer = []
    honor = []
    for s in score:
        h.heappush(honor,s)
        if len(honor) > k:
            h.heappop(honor)
        answer.append(honor[0])
    return answer