# Programmers 힙(Heap) 1. 더 맵게

# 시간복잡도: O(N log N)

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 스코빌 지수 리스트를 힙 형태로 바꿈
    
    while scoville[0] < K: # 제일 첫 번째 수(최솟값)가 K보다 작을 경우에만 반복
        if len(scoville) < 2:
            answer = -1
            break
        # 리스트 길이가 2보다 작다는 것은 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없다는 의미이므로 answer에 -1 저장

        else:
            least = heapq.heappop(scoville)
            least_2 = heapq.heappop(scoville)

            heapq.heappush(scoville, least + least_2 * 2)
            answer += 1
        # 리스트 길이가 2보다 크거나 같을 때는 제일 낮은 스코빌 지수와 두 번째 스코빌 지수를 pop 하여 사용함
        # (제일 낮은 스코빌 지수 + (두 번째로 낮은 스코빌 지수 * 2)) 값을 다시 리스트에 넣음
        # 그리고 answer에 1을 더해 반복문이 끝날 때까지 카운트하여 모든 음식의 스코빌 지수가 K 이상이 되기까지의 최소 횟수를 구함
    
    return answer
