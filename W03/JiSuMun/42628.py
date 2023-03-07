# 힙
# 이중우선순위큐
# 시간복잡도: heap함수들 => O(logN) => N번 => O(NlogN)
from heapq import heappush, heappop, nlargest, heapify
def solution(operations):
    answer = []
    heap = []
    for i in operations:
        if i[0] == 'I': heappush(heap, int(i[2:]))
        else:
            if len(heap) == 0: pass
            elif i[2] == '-': heappop(heap)
            else:
                heap = nlargest(len(heap), heap)[1:]
                heapify(heap)
    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)
    return answer
"""
heapify: 데이터를 자료구조에 넣고 뺄때, heap성질을 유지하게 만들기 위한 함수
nlargest(n, iterable): iterable에서 최댓값 순으로 n개 찾음
heapq는 기본적으로 min heap => heappop은 최솟값삭제
heap에 아무것도 존재하지 않으면 삭제불가하므로 pass
nlargest사용해서 heap을 최댓값 순으로 찾은 뒤, 두 번째 요소부터 가지게 하면 최댓값 삭제하는 것과 같다.
그 후 heapify로 다시 heap구조로 만들어줌
"""