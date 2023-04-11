# Programmers 탐욕법(Greedy) 5. 섬 연결하기

# 시간복잡도: O(n^2 log n)
def solution(n, costs):
    costs = sorted(costs, key=lambda x:x[2])
    connected = set([costs[0][0], costs[0][1]])
    answer = costs[0][2]
    
    while len(connected) != n:
        for i in range(1, len(costs)):
            if costs[i][0] in connected and costs[i][1] in connected:
                continue
            if costs[i][0] in connected or costs[i][1] in connected:
                connected.add(costs[i][0])
                connected.add(costs[i][1])
                answer += costs[i][2]
                break
    return answer

'''
1. 다리 건설 비용을 기준으로 오름차순 정렬한다.
2. 1에서 costs 리스트를 정렬했을 때의 첫 번째 값, 즉 다리 건설 비용이 가장 적을 때 연결되는 두 섬의 번호를 set에 넣고 그 비용을 answer 값으로 설정한다.
3. costs의 두 번째 요소부터 반복문을 돌려 확인한다. 요소 속 두 섬의 번호가 둘 다 set에 있는 경우 이미 연결되어 있다는 뜻이므로 통과한다. 요소 속 두 섬의 번호 중 한쪽만 set에 있는 경우 연결이 되어 있지 않다는 의미이므로 set에 두 섬의 번호를 넣고 그 비용을 answer 값에 더한 후 반복을 멈춘다.
4. 3번 과정을 연결된 섬의 개수가 n이 될 때까지 반복한다.
5. 총 다리 건설 비용을 반환한다.
'''