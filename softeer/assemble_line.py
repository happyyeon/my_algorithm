import sys
input = sys.stdin.readline

N = int(input())
work_time = []
move_time = []
for i in range(N-1):
    a,b,a_move,b_move = map(int,input().split())
    work_time.append([a,b])
    move_time.append([a_move,b_move])
work_time.append(list(map(int,input().split())))

# i번째 작업장에서 최소 시간
dp_a = [work_time[0][0]]*N # A 라인
dp_b = [work_time[0][1]]*N # B 라인

for i in range(1,N):
    a,b = work_time[i]
    a_move,b_move = move_time[i-1]

    dp_a[i] = min(dp_a[i-1] + a, dp_b[i-1] + b_move + a)
    dp_b[i] = min(dp_a[i-1] + a_move + b, dp_b[i-1] + b)

print(min(dp_a[N-1],dp_b[N-1]))
