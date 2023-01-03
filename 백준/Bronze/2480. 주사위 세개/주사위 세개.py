a,b,c = map(int,input().split())
lst = list((a,b,c))
max_num = max(lst,key=lst.count)
if lst.count(max_num) == 3:
    print(10000+max_num*1000)
elif lst.count(max_num) == 2:
    print(1000+max_num*100)
else:
    print(max(lst)*100)