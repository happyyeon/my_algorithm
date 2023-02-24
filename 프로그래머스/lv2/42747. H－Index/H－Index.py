def check(citations,h):
    cnt = 0
    for i in range(len(citations)):
        if citations[i] >= h:
            cnt += 1 
    if cnt >= h:
        return True
    return False

def solution(citations):
    init = len(citations)
    while not check(citations,init):
        init -= 1
    return init