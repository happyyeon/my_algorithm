def calc(start,m,score):
    return min(score[start:start+m])*m

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    start = 0
    while start+m <= len(score):
        answer += calc(start,m,score)
        start += m
    return answer