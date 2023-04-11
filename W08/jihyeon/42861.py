# 42861 (섬 연결하기)
# 시간 복잡도: O(E log E)

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])    # 비용이 가장 낮은 조건들을 먼저 연산하기 위해 비용을 기준으로 오름차순 정렬
    link = set([costs[0][0]])   # 시작 연결점을 set 리스트에 추가

    # Kruskal 알고리즘으로 최소 비용 구하기
    while len(link) != n:   # set 안에 연결된 모든 위치가 연결되기 전까지 실행
        for i in costs:
            if i[0] in link and i[1] in link:   # 두 섬이 이미 더 낮은 가격으로 연결이 되었을 경우
                continue
            if i[0] in link or i[1] in link:    # 두 섬 중 하나가 연결이 되어있지 않을 때
                link.update([i[0], i[1]])   # update로 중복을 제거하며 이미 섬이 연결 되었을 경우 중복된 섬은 추가되지 않고 최대 n 개의 섬을 유지
                answer += i[2]
                break
                
    return answer


# Kruskal 알고리즘 : 탐욕적인 방법(greedy method)을 이용하여 네트워크(가중치를 간선에 할당한 그래프)의 모든 정점을 최소 비용으로 연결하는 최적 해답을 구하는 것
