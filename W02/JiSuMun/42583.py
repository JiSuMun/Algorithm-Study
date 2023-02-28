# 다리를 지나는 트럭
# 스택/큐
# 시간복잡도: O(len(truck_weights) + sum(truck_weights) * bridge_length) => 최악!!
from collections import deque
def solution(bridge_length, weight, truck_weights):
    d = deque(truck_weights)
    bridge = [0]*bridge_length
    sec = 0
    while bridge:
        sec += 1
        bridge.pop(0)
        if d:
            if sum(bridge) + d[0] <= weight:
                bridge.append(d.popleft())
            else:
                bridge.append(0)
    return sec
"""
d: O(len(truck_weights))
while: O(sum(truck_weights) * bridge_length)
bridge.pop(0): O(bridge_length)
sum함수를 사용하면서 시간복잡도가 많이 늘어 효율성이 극히 떨어진다.
bridge 리스트가 빌 때까지 반복한다.
시작하면서 1초 가산, 맨앞을 뽑아준다.
트럭의 무게 리스트 요소가 존재할 때 브리지위에 올라간 무게와 트럭 무게 리스트 첫번째 요소를 더해 다리를 버티는 무게보다 작다면
브리지 리스트에 추가한다.
브렇지 않다면 브리지에 0을 추가해 칸을 채운다.
"""

# 시간복잡도: O(bridge_length + len(truck_weights) + sum(truck_weights))
from collections import deque
def solution(bridge_length, weight, truck_weights):
    d = deque([0] * bridge_length) # 다리 위에 있는 트럭
    wei = deque(truck_weights) 
    sec = 0 
    bridge = 0 # 다리 위에 올라가있는 무게
    while d: 
        sec += 1 
        a = d.popleft() 
        bridge -= a
        if wei: 
            if bridge + wei[0] <= weight: 
                b = wei.popleft() 
                bridge += b
                d.append(b) 
            else: d.append(0) 
    return sec

"""
시간면에서 효율이 상당히 더 높음
d: O(bridge_length)
wei: O(len(truck_weights))
while: O(sum(truck_weights)) => O(N)
O(bridge_length + len(truck_weights) + sum(truck_weights))
로직은 위 풀이와 같으나 sum함수를 사용하지 않고 다리위에 올라간 무게 변수를 따로 주어 더하고 빼도록 했다.
"""