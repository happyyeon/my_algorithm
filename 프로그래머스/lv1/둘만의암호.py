def solution(s, skip, index):
    answer = ''
    skip = set(skip)
    for c in s:
        cnt = 0
        cur = c
        while cnt < index:
            x,y = divmod((ord(cur)+1),ord('z')+1)
            cur = chr(y+x*ord('a'))
            if cur in skip:
                continue
            cnt += 1
        answer += cur
    return answer
