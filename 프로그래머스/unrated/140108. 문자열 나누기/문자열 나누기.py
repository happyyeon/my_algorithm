from collections import deque
def solution(s):
    answer = 0
    first_stack = []
    other_stack = []
    s = deque(s)
    while s:
        if not first_stack:
            first_stack.append(s.popleft())
        else:
            now = s.popleft()
            if now == first_stack[-1]:
                first_stack.append(now)
            else:
                other_stack.append(now)
        if len(first_stack) == len(other_stack):
            answer += 1
            first_stack = []
            other_stack = []
    if first_stack: 
        return answer+1 
    else: 
        return answer