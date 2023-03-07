# 42627 (디스크 컨트롤러)
# 시간 복잡도: while문, 힙 자료구조 사용 - O(NlogN)
import heapq

def solution(jobs):
    answer, now, i = 0,0,0
    start = -1
    heap = []

    while i < len(jobs):    # 각 작업이 언제 요청되었는지 확인
        for j in jobs:
            if start < j[0] <= now: # 만약 현재 시간(now)보다 이전에 요청된 작업이 있다면
                heapq.heappush(heap, [j[1], j[0]])  # 이 작업들을 heap 리스트에 저장 (소요시간을 기준으로 최소힙을 사용하기 때문에 heap에 저장 시 [작업 소요 시간, 작업 요청 시간]으로 저장)

        if len(heap) > 0:   # 처리할 작업이 있다면
            time = heapq.heappop(heap)  # heap 리스트에서 작업을 하나 꺼내면서
            start = now                 # start 변수를 현재 시간(now)로 갱신
            now += time[0]              # now = 현재 시간 + 작업 소요 시간
            answer += now - time[1]     # answer 변수에는 현재 시간에서 요청 시간을 뺀 값을 더해줌
            i += 1                      # i는 현재까지 완료된 작업의 수
        else:               # 처리할 작업이 없다면
            now += 1        # 현재 시간 +1

    return (answer//len(jobs)) # answer 값을 jobs 리스트의 길이로 나누어 평균값 계산 후 반환

