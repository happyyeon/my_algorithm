def update(plyr_rnk,rnk_plyr,call):
    rnk = plyr_rnk[call]
    tmp = rnk_plyr[rnk-1]
    rnk_plyr[rnk-1] = call
    rnk_plyr[rnk] = tmp
    plyr_rnk[call] -= 1
    plyr_rnk[tmp] += 1
    return plyr_rnk,rnk_plyr

def solution(players, callings):
    plyr_rnk = dict()
    rnk_plyr = dict()
    for i in range(len(players)):
        plyr_rnk[players[i]] = i
        rnk_plyr[i] = players[i]
    for c in callings:
        plyr_rnk,rnk_plyr = update(plyr_rnk,rnk_plyr,c)
    return list(map(lambda x: x[0],sorted(plyr_rnk.items(), key=lambda x: x[1])))