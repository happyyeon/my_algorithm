import sys
input = sys.stdin.readline

# time -> minute
def time_to_min(time):
    hour,minute = map(int,time.split(':'))
    return hour*60 + minute

answer = 0
# Input
for _ in range(5):
    start,end = input().split()
    answer += time_to_min(end) - time_to_min(start)

# Output
print(answer)
