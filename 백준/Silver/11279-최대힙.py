import heapq as h
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    heap = []
    for _ in range(N):
        num = int(input())
        if num > 0:
            h.heappush(heap,-num)
        elif not num:
            if heap:
                print(-h.heappop(heap))
            else:
                print(0)
