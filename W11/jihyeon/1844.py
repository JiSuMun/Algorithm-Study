# 1844 (게임 맵 최단거리)
# 시간 복잡도: O(N^2) - BFS 함수는 모든 칸을 한 번씩 방문하며, 상하좌우로 인접한 칸들을 큐에 넣고, 다시 큐에서 꺼내며 방문 처리하는 과정을 거칩니다. 따라서 모든 칸을 한 번씩 방문하므로 시간 복잡도는 O(N^2)이 됩니다.


# bfs 활용
from collections import deque

def solution(maps):
    answer = 0

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def BFS(x, y):
        queue = deque()
        queue.append((x, y))    # 캐릭터가 서 있는 칸

        # queue가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()  # 캐릭터가 서있는 칸의 좌표를 큐에서 꺼내기 (방문 처리)

            # 상하좌우 칸 확인하기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵을 벗어나면 무시
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue

                # 벽을 만나면 무시
                if maps[nx][ny] == 0:  
                    continue

                # 만약 처음 지나가는 길이면 거리를 계산 후 다시 상하좌우 확인하기
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))    

        # 상대 팀 진영(제일 오른쪽 아래 칸)까지의 거리 반환
        return maps[len(maps)-1][len(maps[0])-1]

    answer = BFS(0, 0)
    return -1 if answer == 1 else answer    # 상대 팀 진영에 도착할 수 없으면 -1 반환, 아니면 최종 거리 반환


# 이 문제 또한 비슷한 문제를 본 적이 있지만 개인적으로 어렵게 다가왔다.
