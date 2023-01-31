from collections import defaultdict
n,m = map(int,input().split())
reserve = defaultdict(list)
answer = defaultdict(list)

# 1,2
for i in range(n):
    room = input()
    reserve[room].append(8)
    answer[room]
for i in range(m):
    r,s,t = input().split()
    s,t = int(s),int(t)
    for i in range(s,t):
        reserve[r].append(i)
for r in reserve:
    reserve[r] = sorted(reserve[r])

# 3
for r in reserve:
    for i in range(len(reserve[r])):
        start = reserve[r][i]+1
        if i != len(reserve[r])-1:
            end = reserve[r][i+1]
        else:
            end = 18
        if start == end:
            continue
        if start == 9:
            start = "09"
        else:
            start = str(start)
        end = str(end)
        answer[r].append(start+"-"+end)
# 4
answer = sorted(answer.items(),key= lambda item: item[0])
for i in range(len(answer)):
    room,time = answer[i][0], answer[i][1]
    print("Room {0}:".format(room))
    if time == []:
        print("Not available")
    else:
        print("{0} available:".format(len(time)))
        for t in time:
            print(t)
    if i != len(answer)-1:
        print("-----")
