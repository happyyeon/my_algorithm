import sys
from itertools import combinations as comb
input = sys.stdin.readline

def check_moeum_jaeum(str_lst):
    temp = []
    for i in range(len(str_lst)):
        moeum,jaeum = 0,0
        for j in range(len(str_lst[i])):
            if str_lst[i][j] in {'a','e','i','o','u'}:
                moeum += 1
            else:
                jaeum += 1
        if moeum >= 1 and jaeum >= 2:
            temp.append(str_lst[i])
    return temp

if __name__ == '__main__':
    L,C = map(int,input().split())
    alphas = input().split()
    str_lst = list(comb(alphas,L))
    for i in range(len(str_lst)):
        str_lst[i] = sorted(str_lst[i])
    str_lst = check_moeum_jaeum(str_lst)
    for i in range(len(str_lst)):
        str_lst[i] = ''.join(list(str_lst[i]))
    for answer in sorted(str_lst):
        print(answer)
