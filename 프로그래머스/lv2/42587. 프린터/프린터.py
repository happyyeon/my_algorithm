from collections import deque

def put_index(lst):
    return deque([(val,idx) for idx,val in enumerate(lst)])

def check(priorities):
    for i in range(1,len(priorities)):
        if priorities[0][0] < priorities[i][0]:
            return False
    return True

def solution(priorities, location):
    cnt = 0
    priorities = put_index(priorities)
    
    while True:
        if check(priorities):
            cnt += 1
            if priorities.popleft()[1] == location:
                return cnt
        else:
            priorities.append(priorities.popleft())