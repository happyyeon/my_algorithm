def solution(common):
    answer = 0
    for i in range(2,len(common)):
        if common[i] - common[i-1] == common[i-1] - common[i-2]:
            break
    else:
        return common[-1]*(common[-1]//common[-2])
    return common[-1]+(common[-1]-common[-2])