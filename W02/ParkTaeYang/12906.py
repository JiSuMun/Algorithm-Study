from collections import deque
import copy
def solution(arr):
    dea = deque(arr)
    answer = [dea[0]]
    for i in dea: # deque mutated during iteration 
        num = dea.popleft()
        if answer[-1] != num:
            answer.append(num)
    return answer

print(solution([1,1,3,3,0,1,1]))
# 시간초과 합계: 93.0 / 100.0
# 굳이 데크를 쓸 필요가 없는데 문제 목록이 스택/큐여서 데크를 썼더니 시간초과가 난거같다


def solution(arr):
    answer = [arr[0]]
    for i in arr:
        if answer[-1] != i:
            answer.append(i)
    return answer
#통과
#시간복잡도는 반복문 순환 O(N)