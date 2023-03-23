def convert(string):
    number = 0
    alpha_to_num = dict()
    for i in range(97,124):
        alpha_to_num[chr(i)] = i-96
    for i in range(len(string)):
        number += alpha_to_num[string[i]]*(31**i)
    return number

if __name__ == '__main__':
    L = int(input())
    string = input()
    print(convert(string))