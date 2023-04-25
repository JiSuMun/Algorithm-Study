# 동적계획법(Dynamic Programming)
# 도둑질
# 시간복잡도: O(N)
"""
각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return

1. 각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.

2. 이 마을에 있는 집은 3개 이상 1,000,000개 이하

3. money 배열의 각 원소는 0 이상 1,000 이하인 정수
"""

def solution(money):
    n = len(money)
    dp = [0]*n

    # 첫번째 집 터는 경우
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, n-1):
        dp[i] = max(dp[i-2]+money[i], dp[i-1])
    res1 = dp[-2]
    
    # 첫 번째 집 안터는 경우
    dp[0] = 0
    dp[1] = money[1]
    for i in range(2, n):
        dp[i] = max(dp[i-2]+money[i], dp[i-1])
    res2 = dp[-1]
    return max(res1, res2)

"""
처음에는 홀수, 짝수로 나누어서 풀어야 하나 생각했었다.
하지만 홀수든 짝수든 1번과 마지막집은 인접한다.
그 포인트가 가장 중요한 문제였다.
"""