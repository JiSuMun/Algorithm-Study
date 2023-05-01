
# return 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값
def solution(maps):

    n, m = len(maps), len(maps[0])
    move = [(0, -1), (0, +1), (+1, 0), (-1, 0)]

    
    # BFS
    visited = [[0]*m for _ in range(n)]
    visited[n-1][m-1] = 1

    que = deque([(n-1, m-1)])
    while que:
        x, y = que.popleft()
        dist = visited[x][y]

        # 각 방향에 대해
        for dx, dy in move:
            nx, ny = dx+x, dy+y

            # 이동 가능하다면..
            if nx in range(n) and ny in range(m) and maps[nx][ny]:

                # 목적지 도착
                if nx == 0 and ny == 0:
                    return dist + 1
                
                # 탐색하지 않은 곳 또는 더 좋은 경로 발견
                elif visited[nx][ny] == 0 or visited[nx][ny] > dist + 1:
                    visited[nx][ny] = dist + 1
                    que.append((dx+x, dy+y))

    return -1
                

from collections import deque

# 3) 최단거리 구해야 하는 문제 -> BFS
# 미로 찾기 등 최단거리를 구해야 할 경우, BFS가 유리합니다.
# 왜냐하면 깊이 우선 탐색으로 경로를 검색할 경우 처음으로 발견되는 해답이 최단거리가 아닐 수 있지만, 
# 너비 우선 탐색으로 현재 노드에서 가까운 곳부터 찾기 때문에경로를 탐색 시 먼저 찾아지는 해답이 곧 최단거리기 때문입니다.
                
                

maps, 	answer = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]],	11

print(solution(maps), answer)