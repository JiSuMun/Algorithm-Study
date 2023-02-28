# 42586 (기능개발)
# 시간 복잡도: while문 안에 for문 - O(n log n)
def solution(progresses, speeds):
    cnt = 0
    answer = []

    while progresses:   # progresses 안에 작업이 있을 동안
        if progresses[0] + speeds[0] >= 100:    # 만약 progresses의 첫번째 요소와 speeds의 첫번째 요소의 합이 100과 같거나 100보다 크다면
            progresses.pop(0)   # progresses의 첫번째 요소를 빼고
            speeds.pop(0)       # speeds의 첫번째 요소를 뺀다
            cnt += 1            # 그리고 작업이 하나 완성됐다는 의미로 cnt += 1을 해준다.
        else:                   # 그게 아니라 progresses의 첫번째 요소와 speeds의 첫번째 요소의 합이 100 미만이면
            if cnt:             # 추가로 cnt가 1 이상이면 (앞에 완성된 작업이 하나 이상 있다면)
                answer.append(cnt)  # answer에 cnt를 추가해주고
                cnt = 0             # cnt는 0으로 초기화 시킨다.
            for i in range(len(progresses)):    # cnt가 0이면 (앞에 완성된 작업이 없다면) progresses의 길이로 for문을 돌림
                progresses[i] += speeds[i]      # progresses의 각 요소에 작업 속도를 각각 더해준다.
    answer.append(cnt)  # progresses 안에 작업이 없다면 answer에 cnt를 추가해준다.
    return answer       # answer 반환
