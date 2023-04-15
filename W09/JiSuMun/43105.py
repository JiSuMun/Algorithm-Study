# 동적계획법(Dynamic Programming)
# 정수 삼각형
# 시간복잡도: O(N^2) => dp 리스트를 초기화
"""
삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우

1. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능
    - triangle의 각 요소리스트 값은 인덱스의 같은 값과 다음 값에만 이동 가능

2. 삼각형의 높이는 1 이상 500 이하

3. 삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수

* 그림 그려가며 계산해보고 코드 작성하면 이해 쉬움
"""
def solution(triangle):
    n = len(triangle)
    dp = [[0]*(i+1) for i in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(i+1):
            if j == 0: dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i: dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else: dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    return max(dp[n-1])

"""
- dp[0][0] 은 삼각형 꼭대기값이므로 미리 할당해줌
- 다음 리스트의 첫번째, 마지막 인덱스일 경우부터 미리 계산해줌
- 마지막 dp인덱스의 최대값이 답임
"""