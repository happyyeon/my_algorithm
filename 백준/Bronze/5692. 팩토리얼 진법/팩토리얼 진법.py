def init():
    lst = []
    while True:
        temp = input()
        if not int(temp):
            break
        lst.append(temp)
    return lst

def factorial(num):
    dp = [1]*(num+1)

    for i in range(2,num+1):
        dp[i] = i*dp[i-1]
    return dp[num]

def convert(x):
    num = 0
    for i in range(len(x)):
        num += int(x[i])*factorial((len(x)-i))
    return num

if __name__ == '__main__':
    lst = init()
    for x in lst:
        print(convert(x))