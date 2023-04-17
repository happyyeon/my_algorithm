def binary_search(lst,d):
	start,end = 0,0
	length = 0
	while start < N and end < N:
		if lst[end]-lst[start] <= d:
			length = max(length,end-start+1)
			end += 1
		else:
			start += 1
	return N-length
			
if __name__ == '__main__':
	N,D = map(int,input().split())
	ant = sorted(list(map(int,input().split())))
	print(binary_search(ant,D))
