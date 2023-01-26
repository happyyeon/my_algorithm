import sys
input = sys.stdin.readline

def solution(nums):
    answer = ''
    if nums == [1,2,3,4,5,6,7,8]:
        answer = 'ascending'
    elif nums == [8,7,6,5,4,3,2,1]:
        answer = 'descending'
    else:
        answer = 'mixed'
    return answer

nums = list(map(int,input().split()))
answer = solution(nums)
print(answer)
