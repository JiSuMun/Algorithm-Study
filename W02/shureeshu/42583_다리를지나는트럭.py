
# 다리를 지나는 트럭

from collections import deque

from collections import deque

# O(M+N)
def solution(bridge_length, weight, truck_weights): 
    answer = 0
    bridge = deque([0] * bridge_length)
    current_weight = 0
    trucks = deque(truck_weights)
    while trucks:
        answer += 1
        current_weight -= bridge.popleft()
        if current_weight + trucks[0] <= weight: # if sum(bridge) + trucks[0] <= weight:
            current_weight += trucks[0]
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
    answer += bridge_length
    return answer
