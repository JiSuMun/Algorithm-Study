def solution(n, computers):
    answer = 0
    check = [False for _ in range(n)]

    def dfs(i):
        check[i] = True
        for j in range(n):
            if computers[i][j] == 1 and not check[j]:
                dfs(j)
    
    for i in range(n):
        if not check[i]:
            dfs(i)
            answer += 1
    
    return answer
