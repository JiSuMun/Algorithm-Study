# Programmers 깊이/너비 우선 탐색(DFS/BFS) 2. 네트워크

# 시간복잡도: O(n^2)
from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    computers = deque(computers)

    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True
    
            while queue:
                node = queue.popleft()
                for j in range(n):
                    if computers[node][j] == 1 and not visited[j]:
                        queue.append(j)
                        visited[j] = True
            answer += 1

    return answer

'''
1. 컴퓨터의 연결 여부를 확인하기 위해 컴퓨터의 개수 n개만큼 Fasle 요소를 담은 리스트를 만든다.
2. 1번에서 만든 visited 리스트를 처음부터 확인해 가며 False로 처리된, 즉 연결되지 않은 컴퓨터 번호가 있으면 해당 컴퓨터의 연결 정보가 담긴 2차원 배열 리스트를 불러온다. 그 후 그 컴퓨터에 연결된 모든 컴퓨터를 visited 처리하고 네트워크 개수에 1을 더한다.
3. 2번 과정을 반복하여 네트워크의 총개수를 구한다. 단, 어느 컴퓨터와도 연결되지 않은 컴퓨터가 있을 수 있으며 연결된 컴퓨터가 별개인 그룹이 있을 수 있으므로 각각 개별적으로 하나의 네트워크를 가진다고 봐야 한다.
'''