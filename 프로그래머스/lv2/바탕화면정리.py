def get_min(matrix):
    x = 50
    y = 50
    for i in range(len(matrix)):
        if '#' in matrix[i] and x == 50:
            x = i
        for j in range(len(matrix[i])):
            if matrix[i][j] == '#' and j < y:
                y = j
    return [x,y]

def get_max(matrix):
    x = -1
    y = -1
    for i in range(len(matrix)):
        if '#' in matrix[i] and i > x:
            x = i
        for j in range(len(matrix[i])):
            if matrix[i][j] == '#' and j > y:
                y = j
    return [x+1,y+1]

def solution(wallpaper):
    answer = []
    answer.extend(get_min(wallpaper))
    answer.extend(get_max(wallpaper))
    return answer
