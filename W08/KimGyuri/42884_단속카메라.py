# Programmers 탐욕법(Greedy) 6. 단속카메라

# 시간복잡도: O(n log n)
def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x:x[1])
    camera = -30001

    for i in range(len(routes)):
        if routes[i][0] <= camera:
            continue
        else:
            answer += 1
            camera = routes[i][1]
    return answer

'''
1. 카메라는 차량이 나가는 지점에 설치하는 것이 효율적이므로 진출 지점을 기준으로 routes 리스트를 정렬한다.
2. 카메라가 설치될 위치의 초기 값은 -30,001로 설정한다.
3. 차량의 진입 지점이 카메라가 설치된 지점보다 같거나 작다면 즉, 카메라가 설치된 지점 이전에 진입한다면 카메라를 만날 수 있으므로 통과한다. 만약 그 반대로 차량의 진입 지점이 카메라가 설치된 지점보다 크다면 즉, 카메라가 설치된 지점 이후에 진입한다면 카메라를 만날 수 없으므로 해당 차량이 나가는 진출 지점에 카메라를 한 대 더 설치하고 카메라 위치를 재설정한다.
4. 3을 반복하고 카메라의 개수를 출력한다.
'''