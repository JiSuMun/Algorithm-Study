# 프린터
# 스택/큐
# 시간복잡도: while문 => 최대 O(len(p)), max, for문 => O(N)
# while문의 연산개수에 따라 시간복잡도가 달라짐
from collections import deque
def solution(priorities, location):
    p = deque([(j, i) for i, j in enumerate(priorities)])
    res = 0
    while p:
        a = p.popleft()
        if p and a[0] < max(p)[0]: p.append(a)
        else: 
            res += 1
            if a[1] == location: break
    return res
"""
인덱스를 뒤에 넣어줘야 max값을 구할 때 중요도 순서로 됨
"""