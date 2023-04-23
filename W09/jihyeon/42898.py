# 42898 (등굣길)
# 시간 복잡도: O(nm + k)

def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)] # dp 테이블 초기화
    dp[1][1] = 1
    
    for i, j in puddles: # 웅덩이가 있는 곳은 -1로 표시
        dp[j][i] = -1
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1: # 만약 웅덩이를 만나면
                dp[i][j] = 0 # 이후 값에 영향을 주지 않게 하기 위해 0으로 바꾸고
                continue # 건너뜀
                
            # 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 하라 했으니 나눠주면서 위에서 오는 경우와 왼쪽에서 오는 경우를 더해줌
            dp[i][j] += (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
            
    return(dp[n][m])
