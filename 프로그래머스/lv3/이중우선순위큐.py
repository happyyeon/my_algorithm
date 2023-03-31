import heapq as h

def max_heappop(heap):
    my_max_heap = [-1 * x for x in heap]
    h.heapify(my_max_heap)
    value = -1*h.heappop(my_max_heap)
    my_min_heap = [-1 * x for x in my_max_heap]
    h.heapify(my_min_heap)
    return (value,my_min_heap)
    
def process(heap,command,num):
    if command == 'I':
        h.heappush(heap,num)
    if command == 'D':
        if heap:
            if num == -1:
                h.heappop(heap)
            if num == 1:
                heap = max_heappop(heap)[1]
    return heap

def check(heap):
    if not heap:
        return [0,0]
    return [max_heappop(heap)[0],h.heappop(heap)]

def solution(operations):
    heap = []
    for op in operations:
        command, num = op.split()
        heap = process(heap,command,int(num))
    return check(heap)
