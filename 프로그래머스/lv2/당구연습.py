from math import sqrt
INF = int(1e9)

def get_dist(p0,p1):
    return abs(p0[0]-p1[0])**2+abs(p0[1]-p1[1])**2

def cushion(m,n,x0,y0,x1,y1,flag):
    if flag == 'up':
        if y1 >= y0 and x0 == x1:
            return INF
        return get_dist((x0,2*n-y0),(x1,y1))
    if flag == 'down':
        if y1 <= y0 and x0 == x1:
            return INF
        return get_dist((x0,-y0),(x1,y1))
    if flag == 'left':
        if x1 <= x0 and y0 == y1:
            return INF 
        return get_dist((-x0,y0),(x1,y1))
    if flag == 'right':
        if x1 >= x0 and y0 == y1:
            return INF
        return get_dist((2*m-x0,y0),(x1,y1))

def solution(m, n, startX, startY, ball):
    answer = []
    flag = ['up','down','left','right']
    for i in range(len(ball)):
        tmp = INF
        for f in flag: 
            tmp = min(tmp,cushion(m,n,startX,startY,ball[i][0],ball[i][1],f))
        answer.append(tmp)
    return answer
