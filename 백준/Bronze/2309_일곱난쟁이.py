import sys
from itertools import combinations as comb
input = sys.stdin.readline

if __name__ == '__main__':
    lst = []
    for _ in range(9):
        lst.append(int(input()))
    for x in list(comb(lst,7)):
        if sum(x) == 100:
            for answer in sorted(x):
                print(answer)
            exit()
