from collections import deque
def solution(n, m, section):
    answer = 0
    section = deque(section)
    while section:
        flg = section[0]
        while section and section[0] < flg+m:
            section.popleft()
        answer += 1
    return answer
