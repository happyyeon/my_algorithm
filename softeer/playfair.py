import sys
from collections import deque
def devide(message):
    two_words = list()
    message = deque(message)
    while len(message) >= 2:
        if message[0] != message[1]:
            two_words.append(message.popleft())
            two_words.append(message.popleft())
        else:
            if message[0] != 'X':
                two_words.append(message.popleft()+'X')
            else:
                two_words.append(message.popleft()+'Q')
    if message:
        two_words.append(message[0]+'X')
    message = ''.join(two_words)
    two_words = list()
    for i in range(0,len(message),2):
        two_words.append(message[i:i+2])
    return two_words

def amhohwa(key):
    table = [[0]*5 for _ in range(5)]
    overlap = set()
    alpha = set()
    for i in range(65,91):
        if i == 74:
            continue
        alpha.add(chr(i))
    temp_list = list()
    for k in key:
        if k not in overlap:
            overlap.add(k)
            temp_list.append(k)
    temp_list.extend(sorted(list(alpha-overlap)))
    temp_list = deque(temp_list)
    for i in range(5):
        for j in range(5):
            table[i][j] = temp_list.popleft()
    return table

def amhohwa2(two_words,table):
    answer = []
    for word in two_words:
        for i in range(5):
            for j in range(5):
                if table[i][j] == word[0]:
                    a,b = i,j
                if table[i][j] == word[1]:
                    c,d = i,j
        # Case 1
        if a == c:
            if b != 4 and d != 4:
                answer.append(table[a][b+1]+table[c][d+1])
            elif b == 4 and d != 4:
                answer.append(table[a][0]+table[c][d+1])
            elif b!=4 and d == 4:
                answer.append(table[a][b+1]+table[c][0])
            else:
                answer.append(table[a][0]+table[c][0])
        # Case 2
        elif b == d:
            if a != 4 and c != 4:
                answer.append(table[a+1][b]+table[c+1][d])
            elif a == 4 and c != 4:
                answer.append(table[0][b]+table[c+1][d])
            elif a != 4 and c == 4:
                answer.append(table[a+1][b]+table[0][d])
            else:
                answer.append(table[0][b]+table[0][d])
        # Case 3
        else:
            answer.append(table[a][d]+table[c][b])
    return answer

message = input()
key = input()
two_words = devide(message)
table = amhohwa(key)
answer = amhohwa2(two_words,table)
print(''.join(answer))
