# 탐욕법(Greedy)
# 구명보트
# 시간복잡도: sort => O(NlogN)
"""
1. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한

2. 구명보트를 최대한 적게 사용하여 모든 사람을 구출

3. 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없다.

"""
def solution(people, limit):
    cnt = 0
    people.sort()
    i, j = 0, len(people)-1
    while i <= j:
        cnt += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return cnt
"""
for문으로 풀이를 시작했다가 2중 반복문 이상의 시간복잡도가 예상되어 while문으로 변경
가장 무거운 사람과 가벼운 사람을 더해서 비교 시작
"""