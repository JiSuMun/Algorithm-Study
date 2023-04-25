# Programmers 동적계획법(Dynamic Programming) 4. 사칙연산

# 시간복잡도: O(n^3)
def solution(arr):
    n = len(arr) // 2 + 1
    dp_max = [[-float("inf")] * n for _ in range(n)]
    dp_min = [[float("inf")] * n for _ in range(n)]

    for i in range(n):
        dp_max[i][i] = dp_min[i][i] = int(arr[i * 2])

    for d in range(1, n):
        for i in range(n - d):
            j = i + d
            for k in range(i, j):
                op = arr[k * 2 + 1]
                if op == "+":
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j])
                else:
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k + 1][j])

    return dp_max[0][n - 1]
