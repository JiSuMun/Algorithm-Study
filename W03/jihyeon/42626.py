# 42626 (더 맵게)
# 시간 복잡도: while문, 힙 자료구조 사용 - O(NlogN)
from heapq import *

def solution(scoville, K):
    answer = 0
    heapify(scoville)   # heapify로 scoville 리스트를 힙으로 만듬

    while scoville[0] < K and len(scoville) > 1:    # scoville[0]이 K보다 작고 scoville의 길이가 1보다 클 때 동안
        a = heappop(scoville)   # a에 scoville에서 가장 작은 값을 팝하고 반환
        b = heappop(scoville)   # b에 scoville에서 가장 작은 값을 팝하고 반환
        heappush(scoville, a + b * 2)   # scoville에 계산한 값을 푸시
        answer += 1             # answer에 +1
        
    return answer if scoville[0] >= K else -1
    # 만약 scoville[0]이 k보다 크거나 같으면 answer 반환, 아니면 -1 반환

# 그동안 힙 문제를 잘 풀어보지 않아서 heappop이 가장 작은 항목을 팝하고 반환한다는 것을 알게됨
