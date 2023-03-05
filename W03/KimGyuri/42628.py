# Programmers 힙(Heap) 3. 이중 우선순위 큐

# 시간복잡도: O(NlogN)

import heapq

def solution(operations):
    heap = []

    for i in operations:
        a, b = i.split()
    # 연산 리스트에서 하나씩 요소를 불러와 띄어쓰기를 기준으로 a, b에 따로 저장함

        if a == 'I':
            heapq.heappush(heap, int(b))
        # a 값이 'I'라면 b 값을 heap 리스트에 저장함

        if a == 'D':
            if b == '1':
                try:
                    heap.remove(max(heap))
                except:
                    continue
            # a 값이 'D'이고 b 값이 '1'이면 heap 리스트에서 최댓값을 제거함
            else:
                try:
                    heapq.heappop(heap)
                except:
                    continue
            # a 값이 'D'이고 b 값이 '-1'이면 heap 리스트에서 최솟값을 제거함
            # 리스트가 비어있을 경우 오류가 발생할 수 있으므로 try ~ except 구문을 사용함

    if len(heap) == 0:
        answer = [0,0]
    else:
        answer = [max(heap), heapq.heappop(heap)]
        
    return answer

    # 반복문이 끝나고 heap 리스트가 비어있다면 [0, 0]을 return 하고, 그 외의 경우 [최댓값, 최솟값]을 return 함
