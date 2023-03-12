import sys
from itertools import permutations as perm
input = sys.stdin.readline

def init():
    N = int(input())
    lst = list(map(int,input().split()))
    op = []
    plus,minus,mult,devide = map(int,input().split())
    for i in range(plus):
        op.append('p')
    for i in range(minus):
        op.append('mn')
    for i in range(mult):
        op.append('mp')
    for i in range(devide):
        op.append('d')
    return N,lst,op

def calc(nums,op):
    origin = nums.copy()
    for i in range(len(op)):
        if op[i] == 'p':
            origin[i+1] = origin[i]+nums[i+1]
        if op[i] == 'mn':
            origin[i+1] = origin[i]-nums[i+1]
        if op[i] == 'mp':
            origin[i+1] = origin[i]*nums[i+1]
        if op[i] == 'd':
            if origin[i] < 0:
                origin[i+1] = -((-origin[i])//nums[i+1])
            else:
                origin[i+1] = origin[i]//nums[i+1]
    return origin[-1]

if __name__ == '__main__':
    high = -int(1e9)
    low = int(1e9)
    N,lst,op = init()
    for case in (perm(op,N-1)): # N!
        res = calc(lst,case) # N 
        high = max(high,res)
        low = min(low,res)
    print(high)
    print(low)
