# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     bridge = [0]*bridge_length
#     bridge = deque(bridge)
#     truck = deque(truck_weights)
#     arrive = []
#     cnt = 0
#     while True:
#         a = bridge.popleft()
#         if sum(bridge) + truck[0] < weight:
#             bridge.append(truck.popleft())
#             truck.append(0)
#             cnt +=1
#         else:
#             bridge.append(0)
#             cnt+=1

#         if a != 0:
#             arrive.append(a)    
#         print(bridge)
#         if len(arrive) == len(truck_weights):
#             return cnt


# bl = 2
# w = 10
# t = [7, 4, 5, 6]
# print(solution(bl,w,t))
#시간초과 합계: 92.9 / 100.0



from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = [0]*bridge_length
    bridge = deque(bridge)
    l = len(truck_weights)
    truck = deque(truck_weights)
    arrive_t = 0
    cnt = 0
    bridge_weight = 0
    while True:
        a = bridge.popleft()
        t = truck.popleft()
        bridge_weight += t - a
        if bridge_weight <= weight:
            bridge.append(t)
            truck.append(0)
            #truck이 계속 pop될수있게 0을 추가
            cnt +=1
        else:
            truck.appendleft(t)
            bridge.append(0)
            bridge_weight -= t
            cnt+=1
        if a != 0:
            arrive_t +=1
            if arrive_t == l:
                return cnt
# 통과

# 통과하지 못한 위 코드에서 sum의 복잡도를 줄이기 위해 다리 위의 차 무게를 pop한 값들을 더하고 뺴서 계산
# 그 외 도착한 차의 대수, 트럭의 대수 같이 상수 만 필요한 값들은 반복분 실행전 계산