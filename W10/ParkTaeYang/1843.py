def solution(arr):
    INF = 987654321
    n = len(arr)//2+1
    MIN_DP = [[INF for _ in range(n)] for _ in range(n)]
    MAX_DP = [[-INF for _ in range(n)] for _ in range(n)]

    for i in range(n):
        MIN_DP[i][i] = int(arr[2*i])
        MAX_DP[i][i] = int(arr[2*i])

    for cnt in range(1,n):
        for i in range(n-cnt):
            j = i+cnt
            for k in range(i,j):
                if arr[k*2+1] == '+':
                    MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k]+MAX_DP[k+1][j])
                    MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k]+MIN_DP[k+1][j])
                else:
                    MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k]-MIN_DP[k+1][j])
                    MIN_DP[i][j] = min(MAX_DP[i][j], MIN_DP[i][k]-MAX_DP[k+1][j])

    return MAX_DP[0][n-1]

a = ["1", "-", "3", "+", "5", "-", "8"]
print(solution(a))