def binary_search(sorted_people,limit):
    cnt = 0
    start,end = 0,len(sorted_people)-1
    while start <= end:
        if sorted_people[start]+sorted_people[end] <= limit:
            start += 1
        end -= 1
        cnt += 1
    return cnt

def solution(people, limit):
    return binary_search(sorted(people),limit)

     