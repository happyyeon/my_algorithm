from collections import deque
import sys
input = sys.stdin.readline

def solution(q):
    while len(q) > 1:
        q.popleft()
        q.append(q.popleft())
    return q[0]

if __name__ == '__main__':
    N = int(input())
    q = deque([x for x in range(1,N+1)])
    print(solution(q))
