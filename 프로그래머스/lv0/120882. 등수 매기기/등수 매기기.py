def get_sum(matrix):
    for i in range(len(matrix)):
        matrix[i] = sum(matrix[i])
    return matrix

def get_rank(lst):
    answer = []
    for i in range(len(lst)):
        rank = 1
        for j in range(len(lst)):
            if i==j:
                continue
            if lst[i] < lst[j]:
                rank += 1
        answer.append(rank)
    return answer

def solution(score):
    sum_lst = get_sum(score)
    answer = get_rank(sum_lst)
    return answer