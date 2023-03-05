# 힙
# 더 맵게
# 시간복잡도: O(N log N)
from heapq import heappush, heappop
def solution(scoville, K):
    heap = []
    for i in scoville: heappush(heap, i)
    cnt = 0
    while heap[0] < K:
        try: heappush(heap, heappop(heap) + heappop(heap) * 2)
        except: return -1
        cnt += 1
    return cnt

"""
가장 작은 스코빌 지수가 K 이상이 될때까지 반복
heapq는 가지고 있는 요소를 push, pop할 때마다 자동으로 정렬
반복문을 돌면서 계산할 때마다 다시 heap에 추가
"""
# 시간복잡도: sort => O(N log N)
from collections import deque
def solution(S, K):
    res = 0
    mix_s = deque()
    S.sort()
    scoville = deque(i for i in S)
    while (scoville and scoville[0] < K) or (mix_s and mix_s[0] < K):
        res += 1
        if len(scoville) + len(mix_s) <= 1: return -1
        food = [0]*2
        for i in range(2):
            if scoville and mix_s:
                if scoville[0] < mix_s[0]: food[i] = scoville.popleft()
                else: food[i] = mix_s.popleft()
            elif scoville: food[i] = scoville.popleft()
            else: food[i] = mix_s.popleft()
        mix_s.append(food[0]+food[1]*2)
    return res       
"""
위 풀이보다 효율성테스트를 더 빠른 시간으로 통과
"""