# 42884 (단속카메라)
# 시간 복잡도: O(n log n)

def solution(routes):
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점(진출)을 기준으로 정렬
    camera = -30001 # 문제의 제한사항에서 진입 지점이 -30000 이상부터라 명시했으니 -30001부터 카메라 위치를 찾는다.
    answer = 0

    for i in routes:
        if i[0] > camera:   # 기준(카메라)보다 진입지점이 뒤에 있으면
            answer += 1     # 단속이 안되기에 카메라 개수 + 1
            camera = i[1]   # 새로운 기준은 해당 경로의 진출지점이 된다.

    return answer


# 문제 제한사항을 고려해야 해서 초반에 좀 틀렸던 것 같다.

