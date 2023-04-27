if __name__ == '__main__':
    answer = 0
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(list(map(int,input().split())))
    lst.sort(key=lambda x: (x[1],x[0]))
    end = -1
    for i in range(N):
        if lst[i][0] < end:
            continue
        answer += 1
        end = lst[i][1]
    print(answer)
