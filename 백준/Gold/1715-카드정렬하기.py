import sys
from queue import PriorityQueue
input = sys.stdin.readline

if __name__ == '__main__':
    answer = 0
    N = int(input())
    q = PriorityQueue()
    for _ in range(N):
        q.put(int(input()))
    while q.qsize() != 1:
        tmp = 0
        tmp += q.get()
        tmp += q.get()
        
        q.put(tmp)
        answer += tmp
    print(answer)
