import sys
import math
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    a_lst = list(map(int,input().split()))
    B,C = map(int,input().split())
    answer = N

    for a in a_lst:
        if a-B > 0:
            answer += math.ceil((a-B)/C)
    print(answer)
