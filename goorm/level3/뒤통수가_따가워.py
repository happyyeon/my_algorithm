if __name__ == '__main__':
	n = int(input())
	height = list(map(int,input().split()))
	stack = [height[0]]
	answer = [0]
	for i in range(1,n):
		answer.append(len(stack))
		while stack and stack[-1] <= height[i]:
			stack.pop()
		stack.append(height[i])
	print(*answer)
