# Programmers 깊이/너비 우선 탐색(DFS/BFS) 3. 게임 맵 최단거리

# 시간복잡도: O(N)
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    if maps[n-2][-1] == 0 and maps[-1][m-2] == 0:
        return -1
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    graph = [[-1] * m for _ in range(n)]

    queue = deque()
    queue.append([0, 0])
    graph[0][0] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny, nx])

    return graph[-1][-1]

'''
1. 상대 팀 진영이 도달할 수 없는 곳이면 -1을 반환한다.
2. 1번과 달리 도달할 수 있는 곳이라면 (0, 0) 지점에 출발하며 시작점도 카운트하기 위해 값을 1로 설정한다.
3. 동서남북 방향 중 갈 수 있는 곳의 값을 그 전의 출발점 + 1로 설정하고 덱에 넣어 해당 위치에서 갈 수 있는 모든 곳을 확인한다.
4. 3번 과정을 반복한 뒤 더 이상 갈 수 있는 곳이 없을 때 제일 우측 하단의 값을 반환한다.
'''