# 깊이/너비 우선 탐색(DFS/BFS)
# 게임 맵 최단거리
# 시간복잡도: O(NM)
"""
이 문제도 swea에서 푼 듯한 느낌

ROR 게임은 두 팀으로 나누어서 진행하며, 상대 팀 진영을 먼저 파괴하면 이기는 게임입니다.

각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리

게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return

"""
from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    res = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    def bfs(x, y):
        d = deque()
        d.append((x, y))
        
        while d:
            x, y = d.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    d.append((nx, ny))
        return maps[n-1][m-1]
    res = bfs(0, 0)
    return -1 if res == 1 else res

"""
n(행)과 m(열)을 분리해주지 않아 계속 틀림
"""