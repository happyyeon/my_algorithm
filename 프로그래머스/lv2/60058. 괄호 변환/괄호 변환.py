# 문자열을 u,v로 분리
def separate(p):
    # print('start sep')
    left,right = 0,0
    i = 0 
    while True:
        if left>0 and right>0 and left==right:
            u = p[:i]
            if u == p:
                v = ''
            else:
                v = p[i:]
            break
        if p[i] == '(':
            left += 1
        if p[i] == ')':
            right += 1
        i += 1
    return u,v
# "올바른 괄호 문자열" 검사
def check(u):
    u = list(u)
    stack = list()
    while u:
        stack.append(u.pop())
        if len(stack)>=2 and stack[-1] == '(' and stack[-2] == ')':
            stack.pop()
            stack.pop()
    if stack:
        return False
    return True
# 괄호 방향 뒤집개
def reverse_par(p):
    p = list(p)
    for i in range(len(p)):
        if p[i] == '(':
            p[i] = ')'
        else:
            p[i] = '('
    return ''.join(p)
def solution(p):
    answer = ''
    #1
    if p == '':
        return ''
    #2
    u,v = separate(p)
    # print('u = {0}, v={1}'.format(u,v))
    #3
    if check(u):
        #3-1
        return u+solution(v)
    #4    
    else:
        #4-1
        answer += '('
        #4-2
        answer += solution(v)
        #4-3
        answer += ')'
        #4-4
        answer += reverse_par(u[1:len(u)-1])
    return answer