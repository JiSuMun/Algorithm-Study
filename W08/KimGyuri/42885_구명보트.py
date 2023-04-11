# Programmers 탐욕법(Greedy) 4. 구명보트

# 시간복잡도: O(NlogN)
from collections import deque

def solution(people, limit):
    answer = 0
    queue = deque(sorted(people))
    while queue:
        heavy = queue[-1]
        light = queue[0]
        if len(queue) == 1:
            answer += 1
            break
        if heavy + light <= limit:
            queue.pop()
            queue.popleft()
        else:
            queue.pop()
        answer += 1

    return answer

'''
1. 사람들을 몸무게순으로 정렬한다.
2. 구명보트는 최대 2명만 탈 수 있기 때문에 가장 마지막에 있는 무거운 사람을 먼저 태우고 가능하다면 가장 처음에 있는 가벼운 사람을 같이 태운다.
3. 2번을 반복하는데 가장 마지막과 가장 처음이 같은 사람, 즉 남은 사람이 1명이라면 보트 하나에 태운다.
'''