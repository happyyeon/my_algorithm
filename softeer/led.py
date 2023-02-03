from collections import deque
seven_segment = dict()
seven_segment['0'] = [1,1,1,0,1,1,1]
seven_segment['1'] = [0,0,1,0,0,1,0]
seven_segment['2'] = [1,0,1,1,1,0,1]
seven_segment['3'] = [1,0,1,1,0,1,1]
seven_segment['4'] = [0,1,1,1,0,1,0]
seven_segment['5'] = [1,1,0,1,0,1,1]
seven_segment['6'] = [1,1,0,1,1,1,1]
seven_segment['7'] = [1,1,1,0,0,1,0]
seven_segment['8'] = [1,1,1,1,1,1,1]
seven_segment['9'] = [1,1,1,1,0,1,1]

tc = int(input())
for _ in range(tc):
    # 7segment_a , 7segment_b make
    a,b = map(int,input().split())
    a = str(a)
    b = str(b)
    segment_a = [[0]*7 for _ in range(5)]
    segment_b = [[0]*7 for _ in range(5)]
    idx = 0
    for i in range(5-len(a),5):
        segment_a[i] = seven_segment[a[idx]]
        idx += 1
    idx = 0
    for i in range(5-len(b),5):
        segment_b[i] = seven_segment[b[idx]]
        idx += 1
    
    # switch calculate
    switch = 0
    for i in range(5):
        for j in range(7):
            if segment_a[i][j] != segment_b[i][j]:
                switch += 1
    print(switch)
