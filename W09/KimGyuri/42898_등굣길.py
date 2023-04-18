# Programmers 동적계획법(Dynamic Programming) 3. 등굣길

# 시간복잡도: O(n*m)
def solution(m, n, puddles):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            elif [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[n][m] % 1000000007

'''
1. 0으로 이루어진 배열을 만들되 편의를 위해 n+1 * m+1 크기로 만든다.
2. 집이 있는 곳, 즉 시작점 [1][1]의 값을 1로 설정한다.
3. 학교가 있는 곳, [m][n] 좌표까지 가는데 지나는 각 좌표에는 해당 좌표에 도달할 수 있는 경우의 수(왼쪽 좌표의 값 + 위 좌표의 값)를 값으로 넣는다. 단, 해당 위치가 물에 잠긴 곳이라면 값은 0이다.
4. 학교가 있는 곳의 값을 1,000,000,007로 나눈 나머지를 출력한다.
'''