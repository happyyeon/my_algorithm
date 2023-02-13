import sys
from collections import deque
input = sys.stdin.readline
answer = 0
# node number
def cal_node(H):
    node = 1
    for i in range(H):
        node += 2**(i+1)
    return node

# Input
H,K,R = map(int,input().split())
node = cal_node(H)
tree_matrix = [dict({'L': deque([]),'R':deque([])}) for _ in range(node)]
for i in range(node-2**H,node):
    tree_matrix[i] = deque(list(map(int,input().split())))

# tree dictionary matrix update
day = 1
while day <= R:
    # 부서장
    if tree_matrix[0]['L'] and day%2:
        answer += tree_matrix[0]['L'].popleft()
    if tree_matrix[0]['R'] and not day%2:
        answer += tree_matrix[0]['R'].popleft()
    
    # 중간급 직원
    for i in range(1,node-2**H):
        if day%2 and i%2 and tree_matrix[i]['L']:
            tree_matrix[(i-1)//2]['L'].append(tree_matrix[i]['L'].popleft())
        if day%2 and not i%2 and tree_matrix[i]['L']:
            tree_matrix[(i-1)//2]['R'].append(tree_matrix[i]['L'].popleft())
        if not day%2 and i%2 and tree_matrix[i]['R']:
            tree_matrix[(i-1)//2]['L'].append(tree_matrix[i]['R'].popleft())
        if not day%2 and not i%2 and tree_matrix[i]['R']:
            tree_matrix[(i-1)//2]['R'].append(tree_matrix[i]['R'].popleft())
    # 말단 노드
    for i in range(node-2**H,node):
        if tree_matrix[i] and i%2:
            tree_matrix[(i-1)//2]['L'].append(tree_matrix[i].popleft())
        if tree_matrix[i] and not i%2:
            tree_matrix[(i-1)//2]['R'].append(tree_matrix[i].popleft())
    day += 1
# Output
print(answer)
