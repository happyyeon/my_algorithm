import sys
input = sys.stdin.readline

num_ijk = 0
n = int(input())
int_list = list(map(int,input().split()))
ox_matrix = [['O']*n for _ in range(n)]

for i in range(n):
    for j in range(i,n):
        if int_list[i] > int_list[j]:
            ox_matrix[i][j] = 'X'
for i in range(n-2):
    circle = 0
    for j in range(i+1,n):
        if ox_matrix[i][j] == 'O':
            circle += 1
        else:
            num_ijk += circle
print(num_ijk)
