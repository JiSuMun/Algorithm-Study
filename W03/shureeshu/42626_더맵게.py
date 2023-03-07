# 더맵게

"""
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville
원하는 스코빌 지수 K

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

return 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수

제한 사항
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
"""

def main():
    input_data = [1, 2, 3, 9, 10, 12], 7
    print(solution(*input_data))


from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer = 0
    
    # O(len(scoville)))
    heapify(scoville) 
    
    # O(len(scoville)) : worst_case
    while scoville: 
        s1 = heappop(scoville)
        if s1 >= K:
            return answer
        if scoville:
            s2 = heappop(scoville)
            heappush(scoville, s1+2*s2)
            answer += 1
        else:
            return -1

main()