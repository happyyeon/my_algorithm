import sys
from collections import deque
input = sys.stdin.readline

def init():
    N = int(input())
    queue_list = [deque([]),deque([]),deque([]),deque([])]
    for i in range(N):
        t,w = input().split()
        queue_list[ord(w)-65].append((i+1,int(t)))
    return N,queue_list

def car_out(waiting_list,cur_time,answer_list):
    for i in range(4):
        if waiting_list[i] and not waiting_list[(i-1)%4]:
            answer_list[queue_list[i].popleft()[0]] = cur_time  
    return answer_list

def solution(queue_list):
    answer_list = [-1]*(N+1)
    cur_time = 0
    while queue_list[0] or queue_list[1] or queue_list[2] or queue_list[3]:
        min_time = int(1e9)
        waiting_list = [False]*4
        for i in range(4):
            if queue_list[i]:
                time = queue_list[i][0][1]
                min_time = min(min_time,time)
                if time <= cur_time:
                    waiting_list[i] = True
        if sum(waiting_list) == 4:
            break
        if sum(waiting_list) == 0:
            cur_time = min_time
            continue
        answer_list = car_out(waiting_list,cur_time,answer_list)
        cur_time += 1
    return answer_list

if __name__ == '__main__':
    N,queue_list = init()
    answer_list = solution(queue_list)
    print(*answer_list[1:],sep='\n')
