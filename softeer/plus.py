import sys
input = sys.stdin.readline

for i in range(int(input())):
    a,b = map(int,input().split())
    print("Case #{0}: {1}".format(i+1,a+b))
