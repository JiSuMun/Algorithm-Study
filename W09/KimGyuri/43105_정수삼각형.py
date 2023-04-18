# Programmers 동적계획법(Dynamic Programming) 2. 정수 삼각형

# 시간복잡도: O(n^2)
def solution(triangle):
    dp = [[0 for _ in range(i+1)] for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        dp[i][0] = triangle[i][0] + dp[i-1][0]
        dp[i][-1] = triangle[i][-1] + dp[i-1][-1]

        for j in range(1, i):
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    
    return max(dp[-1])

'''
1. 삼각형과 동일한 형태이지만 0으로 채워진 배열을 만든다.
    [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]
2. 삼각형의 제일 윗부분, 즉 배열의 [0][0] 값을 삼각형의 꼭대기 숫자 값으로 설정한다.
    [[7], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]
3. 나머지 배열에 대해서는 위에서부터 합쳐 내려온 숫자 중 최댓값으로 바꾼다. 단, 배열의 제일 첫 번째와 마지막 요소는 각각 제일 처음, 마지막 요소만을 이어받을 수 있다.
    [[7], [10, 15], [18, 16, 15], [20, 25, 20, 19], [24, 30, 27, 26, 24]]
4. 마지막 줄의 최댓값을 출력한다.
    30
'''