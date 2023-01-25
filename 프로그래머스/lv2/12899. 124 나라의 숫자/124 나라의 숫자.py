def solution(n):
    answer = list()
    while n:
        n,remain = divmod(n,3)
        if remain == 1:
            answer.append('1')
        elif remain == 2:
            answer.append('2')
        else:
            answer.append('4')
            n -= 1
    answer = ''.join(reversed(answer))
    return answer