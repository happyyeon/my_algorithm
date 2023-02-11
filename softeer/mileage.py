import sys
input = sys.stdin.readline

# Input
A,B = map(int,input().split())

# Output
if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('same')
