def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    i = 0
    nxt = targets[0][1]
    while i < len(targets):
        if targets[i][0] < nxt:
            i += 1
            continue
        nxt = targets[i][1]
        answer += 1
    return answer+1
