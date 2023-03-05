# Programmers 힙(Heap) 2. 디스크 컨트롤러

# 시간복잡도: O(NlogN)
import heapq

def solution(jobs):
    answer = 0 # 작업하는데 걸린 총시간
    start = -1 # 이전에 완료한 작업의 시작 시간
    now = 0 # 현재 시간(시점)
    i = 0 # 처리된 작업의 개수

    heap = [] # 현재 처리 가능한 jobs를 담는 힙
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now: # 작업 요청 시점이 이전에 끝낸 작업보다 크고 현재 시간보다 작을 경우 작업 가능함
                heapq.heappush(heap, [job[1], job[0]]) # (처리 시간, 요청 시간) 형태로 힙에 저장함
        
        if len(heap) > 0: # 힙에 처리할 작업이 남은 경우
            current = heapq.heappop(heap) #cur은 현재 처리 중인 작업
            start = now
            now += current[0]
            answer += (now - current[1]) # 작업 요청 시간으로부터 처리 완료까지의 시간을 계산하여 answer에 저장함
            i += 1
    
        else: # 처리할 작업이 없는 경우
            now += 1
            
    return answer // len(jobs) # 평균 처리 시간 계산
