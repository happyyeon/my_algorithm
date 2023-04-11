import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def union(a,b,parent):
    a = find(a,parent)
    b = find(b,parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(node, parent):
    if node != parent[node]:
        parent[node] = find(parent[node], parent)
    return parent[node]

if __name__ == '__main__':
    n,m = map(int,input().split())
    parent = [i for i in range(n+1)]
    for _ in range(m):
        cmd,a,b = map(int,input().split())

        if cmd:
            if find(a,parent) == find(b,parent):
                print('YES')
            else:
                print('NO')
        else:
            union(a,b,parent)
