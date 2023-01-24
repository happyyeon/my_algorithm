def solution(s):
    answer = True
    s = list(s)
    left,right = 0,0
    while s:
        cur = s.pop()
        if cur == '(':
            left += 1
        else:
            right += 1
        if left > right:
            answer = False
            break
    if left != right:
        answer = False
    return answer