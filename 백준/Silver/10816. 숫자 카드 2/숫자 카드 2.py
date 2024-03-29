from collections import defaultdict
from collections import Counter
def init():
        N = int(input())
        n_lst = sorted(list(map(int,input().split())))
        M = int(input())
        m_lst = (list(map(int,input().split())))
        return N,n_lst,M,m_lst

def binary_search(lst,m):
        start = 0
        end = len(lst)

        while start < end:
                mid = (start+end)//2
                if lst[mid] == m:
                        return True
                if lst[mid] > m:
                        end = mid
                if lst[mid] < m:
                        start = mid+1
        return False

if __name__ == '__main__':
    answer = []
    N,n_lst,M,m_lst = init()
    nums_how_many = Counter(n_lst) # 10^7
    for m in m_lst: # 10^7
        if binary_search(n_lst,m): # log10^7 = 7
                answer.append(nums_how_many[m])
        else:
               answer.append(0)
    print(*answer)
    