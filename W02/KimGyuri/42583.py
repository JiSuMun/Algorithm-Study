# Programmers 스택/큐 5. 다리를 지나는 트럭

# 시간복잡도: O(N)

from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    answer = 0
    bridge_weight = 0

    while bridge:
        answer += 1
        bridge_weight -= bridge.popleft()

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                bridge_weight += truck
            else:
                bridge.append(0)
    
    return answer

'''
1. 대기 트럭 리스트 'truck_weights'를 덱에 넣고 다리를 건너는 트럭을 확인하기 위해 다리 길이만큼 0으로 채워진 bridge 덱을 만든다.
2. 시간을 1씩 카운트하며 무게를 초과하지 않는 한 트럭을 다리에 한 대씩 올린다.
3. 무게를 초과할 경우 덱의 맨 뒤에 빈자리를 나타내는 의미의 0을 추가하며 다리 위의 트럭을 앞으로 밀어낸다.
4. 이 과정을 대기 트럭 리스트뿐 아니라 다리를 건너는 트럭을 나타내는 bridge 덱이 빌 때까지 반복한다.
5. 모든 트럭이 다리를 건너는 데 든 시간을 출력한다.
'''
