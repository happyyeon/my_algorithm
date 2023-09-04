from collections import Counter

def solution(topping):
    answer = 0
    tmp1 = Counter(topping)
    tmp2 = set()
    for i in topping:
        tmp1[i] -= 1
        if not tmp1[i]:
            del tmp1[i]
        tmp2.add(i)
        if len(tmp1) == len(tmp2):
            answer += 1
    return answer
