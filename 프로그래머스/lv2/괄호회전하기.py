from collections import deque
def check(s):
    q = deque([x for x in s])
    stack = []
    pair = {']':'[', '}':'{', ')':'('}
    while q:
        cur = q.popleft()
        if cur in pair and stack and stack[-1] == pair[cur]:
            stack.pop()
        else:
            stack.append(cur)
    if stack:
        return 0
    return 1
            
def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)-1):
        answer += check(s)
        s.append(s.popleft())
    return answer
