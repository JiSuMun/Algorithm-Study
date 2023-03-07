# 힙
# 디스크 컨트롤러
# 시간복잡도: while => N 번, heappush(),heappop() => O(log N), 따라서 O(N log N)
from heapq import heappush, heappop
def solution(jobs):
    res, now, cnt = 0, 0, 0 # 평균값, 현재시간, 작업개수
    start = -1 # 앞에 완료한 작업의 시작 시간
    heap = []
    while cnt < len(jobs):
        for i in jobs:
            if start < i[0] <= now: heappush(heap, [i[1], i[0]])
        if len(heap) > 0:
            cur = heappop(heap)
            start = now
            now += cur[0]
            res += (now - cur[1])
            cnt += 1
        else: now += 1
    return int(res/len(jobs))

"""
시작은 0부터이기때문에 초기값을 -1로 설정
반복문을 돌리는 조건은 작업완료한 개수가 작업해야할 개수보다 적을 때
작업 소요 시간 기준으로 힙을 만들어야 하기 때문에 시점과 소요 시간을 반대로 해서 heappush함
반복할 때마다 시작지점은 현재시간으로 초기화해줌
총 시간은 현재 시점에서 요청시점을 뺀 값을 더하는 것
작업을 한 번 할 때마다 cnt를 +1해줌
더 이상 힙에 남은 요소가 없다면 남아 있는 작업의 요청 시간이 남았기 때문에 현재 시점을 +1 해줌
"""