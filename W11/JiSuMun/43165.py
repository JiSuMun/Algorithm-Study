# 깊이/너비 우선 탐색(DFS/BFS)
# 타겟 넘버
# 시간복잡도: O(2^n)
"""
1. n개의 음이 아닌 정수들 => 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버

2. 주어지는 숫자의 개수는 2개 이상 20개 이하

3. 각 숫자는 1 이상 50 이하인 자연수

4. 타겟 넘버는 1 이상 1000 이하인 자연수

"""
from collections import deque
def solution(numbers, target):
    d = deque([(0, 0)])
    cnt = 0
    while d:
        c_sum, idx = d.popleft()
        if idx == len(numbers):
            if c_sum == target:
                cnt += 1
        else:
            d.append((c_sum + numbers[idx], idx + 1))
            d.append((c_sum - numbers[idx], idx + 1))
    return cnt

"""
방법의 개수를 찾는 것이므로 cnt += 1로 개수를 세어줌
d안에 합계와 인덱스를 튜플로 넣어서 반복문을 돌면서 함께 저장하며 비교
+, -를 적절히 해주는 것이므로 두 가지 방법모두 저장하여 비교
"""