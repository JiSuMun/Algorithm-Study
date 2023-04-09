# people : 사람들의 몸무게를 담은 배열 (정수)
# limit : 구명보트의 무게 제한 (정수)
# return : 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값 (정수)

## 중요 포인트 !! 한 보트에 2명까지 밖에 못 탐..
def solution(people, limit):
    answer = 0
    
    # 무거운 순으로 정렬
    people.sort(reverse=True)
    
    # boat[w] = 무게 제한까지 w만큼 여유 있는 보트의 수
    boat = []
    
    for wp in people:
        # 1. 무게 제한의 절반 보다 무거운 사람들은 서로 같은 보트에 탈 수 없다.
        if wp > limit - wp:
            boat.append(limit - wp)
        # 2. boat[-1] 은 1명씩 타고 있는 보트 중 무게 여유가 가장 큰 보트이다.
        elif boat[-1] >= wp:
            boat.pop()
            answer += 1
        else:
            boat.append(limit - wp)
    
    return answer + len(boat)