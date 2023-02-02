import sys
input = sys.stdin.readline

m,n,k = map(int,input().split())
secret_list = list(map(int,input().split()))
input_list = list(map(int,input().split()))
kind = 'normal'

if n < m:
    print(kind)
    exit(0)
for i in range(0,n-m+1):
    if input_list[i:i+m] == secret_list:
        kind = 'secret'

print(kind)
