# Programmers 완전탐색 5. 피로도

# 시간복잡도: O(n^2 * n!)

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for case in permutations(dungeons, len(dungeons)):
        cnt = 0
        energy = k

        for minimum, cost in case:
            if energy >= minimum:
                cnt += 1
                energy -= cost

        if cnt > answer:
            answer = cnt
    
    return answer

'''
1. permutations 함수를 활용해 던전 순서의 모든 조합을 만든다.
2. 만들어진 조합을 하나씩 불러오며 해당 순서로는 주어진 에너지로 최대 몇 개의 던전을 돌 수 있는지 카운트한다.
3. 최대 던전 수가 answer에 담긴 값보다 클 경우 갱신한다.
'''
