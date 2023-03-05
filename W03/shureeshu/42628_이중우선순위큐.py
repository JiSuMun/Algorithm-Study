# 이중우선순위큐

import heapq 
def solution(operations):
    heap = []
    for s in operations:
        cmd, x = s.split()
        eval(f'{cmd}(heap, {x})')
    
    if heap:
        answer = [heap[-1], heap[0]]
    else:
        answer = [0, 0]
    return answer

# operation "I"
# maxitem을 배열 끝에 유지하는 변형 heappush
def I(heap, item):
    if heap and heap[-1] > item:
        maxitem = heap.pop()
        heapq.heappush(heap, item)
        heap.append(maxitem)
    else:
        heap.append(item)

# operation "D" or "D"
# maxitem을 배열 끝에 유지하는 변형 heappop
def D(heap, x):
    if heap:
        if x > 0:
            heap.pop()
            if heap:
                maxitem = max(heap)
                lastitem = heap.pop()
                if lastitem < maxitem:
                    pos = len(heap)-heap[::-1].index(maxitem)-1
                    while pos > 0:
                        parentpos = (pos-1) >> 1
                        parent = heap[parentpos]
                        if lastitem < parent:
                            heap[pos] = parent
                            pos = parentpos
                            continue
                        break
                    heap[pos] = lastitem
                heap.append(maxitem)
        else:
            heapq.heappop(heap)            
            
input_data = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]     
print(solution(input_data))


"""

시간 복잡도 분석을 해보겠습니다.
이 알고리즘은 먼저 입력된 연산 리스트 operations의 길이를 n이라고 합니다.
solution 함수 내에서 heap을 초기화하는 부분은 O(1)입니다.
for 루프에서 각 연산에 대해 O(log n)의 시간 복잡도를 가지는 eval(f'{cmd}(heap, {x})')를 호출하게 됩니다. 따라서 전체적인 시간 복잡도는 O(n log n)입니다.

I 함수는 아래와 같이 구성됩니다.

heap[-1] 연산: O(1)
heap.pop() 연산: O(log n)
heapq.heappush(heap, item) 연산: O(log n)
heap.append(maxitem) 연산: O(1)
따라서 I 함수의 시간 복잡도는 O(log n)입니다.

D 함수는 아래와 같이 구성됩니다.

heap.pop() 연산: O(log n)
max(heap) 연산: O(n)
heap.pop() 연산: O(log n)
heap.append() 연산: O(1)
while 루프에서 수행되는 연산: O(log n)
따라서 D 함수의 시간 복잡도는 O(n + log n)입니다.

따라서 이중우선순위큐 알고리즘 전체의 시간 복잡도는 O(n log n)입니다.

"""