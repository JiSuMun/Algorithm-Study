# 깊이/너비 우선 탐색(DFS/BFS)
# 네트워크
# 시간복잡도: O(N^2)
"""
swea의 마을 개수 관련 문제와 비슷하다고 느낌

1. 컴퓨터의 개수 n은 1 이상 200 이하인 자연수

2. 각 컴퓨터는 0부터 n-1인 정수로 표현

3. i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현

4. computer[i][i]는 항상 1
"""
def dfs(idx, visited, computers):
    visited[idx] = True
    for nei in range(len(computers)): 
        if not visited[nei] and computers[idx][nei]: 
            dfs(nei, visited, computers)

def solution(n, computers):
    cnt = 0   
    visited = [False] * n   

    for idx in range(n):
        if not visited[idx] :
            dfs(idx, visited, computers)
            cnt += 1 

    return cnt

"""
방문하지 않았고, 컴퓨터사이에 연결이 있으면 dfs 진행
dfs가 끝날때마다 네트워크 += 1
"""