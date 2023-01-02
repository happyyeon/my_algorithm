while True:
    num = str(input())
    if num == '0':
        exit(0)
    if len(num)%2 == 1:
        if num[:len(num)//2] == ''.join(reversed(num[len(num)//2+1:])):
            print('yes')
        else:
            print('no')
    else:
        if num[:len(num)//2] == ''.join(reversed(num[len(num)//2:])):
            print('yes')
        else:
            print('no')

