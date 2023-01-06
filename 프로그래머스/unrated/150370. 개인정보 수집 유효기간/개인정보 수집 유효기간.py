def cal_to_idx(calendar):
    year,month,day = map(int,calendar.split('.'))
    return (year-2000)*336+(month-1)*28+(day-1)

def get_day(terms,privacies):
    end = []
    alpha_num = dict()
    idx_priv = []
    for t in terms:
        alpha, num = t.split()
        alpha_num[alpha] = int(num)
    for p in privacies:
        calendar,alpha = p.split()
        end.append(cal_to_idx(calendar)+28*alpha_num[alpha])
    return end

def is_fire(today,end):
    answer = []
    cur = cal_to_idx(today)
    for i in range(len(end)):
        if cur >= end[i]:
            answer.append(i+1)
    return answer

def solution(today, terms, privacies):
    end = get_day(terms,privacies)
    return is_fire(today,end)