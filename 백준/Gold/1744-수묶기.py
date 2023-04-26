def calc(lst):
    cnt = 0
    i = 0
    while i < len(lst):
        if i == len(lst)-1:
            if lst[i] < 0 and zero:
                break
            else: 
                cnt += lst[i]
                i += 1
        else:
            cnt += (lst[i]*lst[i+1])
            i += 2
    return cnt

if __name__ == '__main__':
    answer = 0
    N = int(input())
    minus = []
    plus = []
    one = []
    zero = False
    for _ in range(N):
        num = int(input())
        if num < 0:
            minus.append(num)
        elif num  == 1:
            one.append(num)
        elif num > 1:
            plus.append(num)
        else:
            zero = True
    minus.sort()
    plus.sort(reverse=True)
    answer += calc(minus)
    answer += calc(plus)
    answer += sum(one)
    print(answer)
