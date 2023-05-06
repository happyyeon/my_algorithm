from collections import deque
def get_num(keymap,c):
    keymap = list(map(deque,keymap))
    cnt = 0
    while sum(list(map(len,keymap))):
        for k in keymap:
            if k and k.popleft() == c:
                return cnt+1
        cnt += 1
    return -1

def solution(keymap, targets):
    answer = []
    for t in targets:
        tmp = []
        for c in t:
            tmp.append(get_num(keymap,c))
        if -1 in tmp:
            answer.append(-1)
        else:
            answer.append(sum(tmp))
    return answer
