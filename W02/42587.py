from collections import deque
import copy
def solution(priorities, location):
    check = []
    le = len(priorities)
    for i in range(le):
        check.append(i)
    # 숫자들의 위치를 알려주는 배열 생성
    deq = copy.deepcopy(priorities)
    deq = deque(deq)
    check = deque(check)
    while True:
        a = deq.popleft()
        num = check.popleft()
        # 맨앞의 숫자와 위치를 뽑아서
        for i in deq:
            if i>a:
                deq.append(a)
                check.append(num)
                break
            #리스트에 뽑은 숫자보다 큰 수가 있다면 맨뒤에 추가
        else:
            if num == location:
                answer = le - len(check)
                break
        # 큰 수가 없다면 위치를 확인하고 몇번쨰로 인쇄했는지 반환
    return answer

# 