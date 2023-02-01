import sys
input = sys.stdin.readline

def make_cp(standard,test):
    cp = set()
    cp_std = []
    cp_tst = []
    x = 0
    for i in range(len(standard)):
        x += standard[i][0]
        cp_std.append(x)
        cp.add(x)
    x = 0
    for i in range(len(test)):
        x += test[i][0]
        cp_tst.append(x)
        cp.add(x)
    cp = sorted(list(cp))
    return cp,cp_std,cp_tst

n,m = map(int,input().split())
standard = list()
test = list()
for i in range(n):
    dist,velo = map(int,input().split())
    standard.append((dist,velo))
for i in range(m):
    dist,velo = map(int,input().split())
    test.append((dist,velo))
cp,cp_std,cp_tst = make_cp(standard,test)
max_velocity = 0
for i in range(len(cp)):
    for j in range(len(cp_std)):
        if cp[i] <= cp_std[j]:
            v1 = standard[j][1]
            break
    for j in range(len(cp_tst)):
        if cp[i] <= cp_tst[j]:
            v2 = test[j][1]
            break
    max_velocity = max(max_velocity,v2-v1)
if max_velocity < 0:
    max_velocity = 0
print(max_velocity)
