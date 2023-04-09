import sys
input = sys.stdin.readline

def move(dice,c):
    if c == 1:
        tmp = [dice['up'], dice['right'], dice['down'], dice['left']]
        dice['right'] = tmp[0]
        dice['down'] = tmp[1]
        dice['left'] = tmp[2]
        dice['up'] = tmp[3]
    if c == 2:
        tmp = [dice['up'], dice['left'], dice['down'], dice['right']]
        dice['left'] = tmp[0]
        dice['down'] = tmp[1]
        dice['right'] = tmp[2]
        dice['up'] = tmp[3]
    if c == 3:
        tmp = [dice['up'], dice['back'], dice['down'], dice['front']]
        dice['back'] = tmp[0]
        dice['down'] = tmp[1]
        dice['front'] = tmp[2]
        dice['up'] = tmp[3]
    if c == 4:
        tmp = [dice['up'], dice['front'], dice['down'], dice['back']]
        dice['front'] = tmp[0]
        dice['down'] = tmp[1]
        dice['back'] = tmp[2]
        dice['up'] = tmp[3]

    return dice

def copy_dc(dice,graph):
    x,y = dice['locate']

    if not graph[nx][ny]:
        graph[x][y] = dice['down']
    else:
        dice['down'] = graph[x][y]
        graph[x][y] = 0
    
    return dice,graph

if __name__ == '__main__':
    N,M,x,y,K = map(int,input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int,input().split())))
    command = list(map(int,input().split()))
    
    dice = {
        'front':0,'back':0, 'left':0, 'right':0, 'up':0, 'down':0, 'locate':(x,y)
    }
    dxy = [(0,1),(0,-1),(-1,0),(1,0)]
    for c in command:
        x,y = dice['locate']
        nx,ny = x+dxy[c-1][0],y+dxy[c-1][1]
        if 0<=nx<N and 0<=ny<M:
            dice['locate'] = (nx,ny)
            dice = move(dice,c)
            dice,graph = copy_dc(dice,graph)
            print(dice['up'])
