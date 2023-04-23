# 42898_등굣길

def solution(m, n, puddles):
    answer = 0
    
    map = [[1]*(m+1) for _ in range(n+1)]
    
    for x, y in puddles:
        map[y][x] = 0
        
    for i in range(1, n+1):
        map[i][1] = map[i][1]*map[i-1][1]
    
    for j in range(1, m+1):
        map[1][j] = map[1][j]*map[1][j-1]
        
    for x in range(4, n+m+1):
        for y in range(2, x - 1):
            i, j = y, x - y
            if 2<= i <= n and 2 <= j <= m and map[i][j]:
                map[i][j] = (map[i][j-1] + map[i-1][j])%1000000007
                
    return map[n][m]

# 시간 복잡도: O(nm)

# 격자 초기화: map = [[1]*(m+1) for _ in range(n+1)]에서 격자를 초기화하는 데 O(nm) 시간이 걸립니다.
# 웅덩이 표시: for x, y in puddles: 루프에서 최대 웅덩이 수만큼 반복되며, 웅덩이를 표시하는 데 O(1) 시간이 걸립니다. 따라서 전체 시간 복잡도는 O(p)입니다 (여기서 p는 웅덩이 수).
# 경로 개수 계산:
# 첫 번째 행과 열의 경로 개수 계산: 각각 O(n)과 O(m) 시간이 걸립니다.
# 나머지 격자 칸의 경로 개수 계산: 격자의 크기에 비례하는 루프를 실행하므로 전체 시간 복잡도는 O(nm)입니다.
# 따라서 전체 시간 복잡도는 O(nm) + O(p) + O(n) + O(m) + O(nm) = O(2nm + p + n + m)입니다. 여기서 가장 큰 항은 nm이므로, 전체 시간 복잡도는 O(nm)으로 근사할 수 있습니다. 여기서 n과 m은 격자의 크기를 나타냅니다.

m,	n,	puddles = 4,	3,	[[2, 3], [3, 4]]
print(solution(m, n, puddles))