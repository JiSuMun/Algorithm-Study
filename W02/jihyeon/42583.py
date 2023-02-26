# 42583 (다리를 지나는 트럭)
# 시간 복잡도: while문 - O(N)
def solution(bridge_length, weight, truck_weights):
    answer = 0  # 경과 시간
    b = [0 for _ in range(bridge_length)]   # 다리 길이만큼의 리스트 생성
    
    while b:    # b안의 값이 있는 동안(차들이 다리를 건너는 동안)
        answer += 1     # 시간 +1초
        b.pop(0)        # 리스트b의 맨 앞 값 삭제
        
        if truck_weights:   # 만약 트럭 무게 리스트안에 값이 있다면
            if sum(b) + truck_weights[0] <= weight: # 추가로 현재 다리를 건너고 있는 차의 무게 합(sum(b))과 대기하고 있는 첫번째 트럭(트럭 무게 리스트 첫번째 값)의 합이 weight를 넘지 않는다면
                b.append(truck_weights.pop(0))      # b(다리 길이)에 대기하고 있는 첫번째 트럭을 추가해준다.
            else:                                   # 그게 아니라 현재 다리를 건너고 있는 차의 무게 합(sum(b))과 대기하고 있는 첫번째 트럭(트럭 무게 리스트 첫번째 값)의 합이 weight를 넘는다면
                b.append(0)                         # 대기하고 있는 첫번째 트럭은 다리를 건널 수 없고 현재 다리를 건너고 있는 차가 다리를 다 건널 때 까지 기다려야 하므로
                                                    # b에 0을 추가해준다.
    return answer   # answer값 반환

        