# 완전탐색
# 전력망을 둘로 나누기
# 시간복잡도: O(N^2 + NE)
# defaultdict에 대한 간단한 설명은 etc 폴더에 넣었습니다.
"""
solution 함수 => O(N)입니다.
visited 리스트 초기화 => O(N)

defaultdict를 생성하는 데 걸리는 시간은 원소의 수에 비례합니다. 이 경우 원소의 수는 각 노드마다 연결된 간선의 개수를 나타내므로, wires 리스트에 있는 간선의 수에 비례합니다. 즉, defaultdict를 생성하는 데 필요한 시간 복잡도는 O(E)입니다.

bfs 함수는 노드의 수 N에 비례하는 루프를 수행하며, 루프 내에서는 각 노드에 대해 연결된 노드를 모두 확인합니다. 이 때문에 bfs 함수의 시간 복잡도는 O(N + E)입니다.

cnt_li 리스트에 대한 루프는 노드의 수 N에 비례합니다. 각 노드에 대해 bfs 함수를 호출하므로, 이 루프의 시간 복잡도는 O(N^2 + NE)입니다.

res 값을 업데이트 => O(1)입니다.

따라서 solution 함수의 전체 시간 복잡도는 O(N^2 + NE)입니다.

위 코드는 간선의 수가 적을 때는 효율적이지만, 간선의 수가 많을 경우에는 연산 비용이 많이 증가하므로, 큰 그래프에서는 느릴 수 있습니다.
"""
# wires는 길이가 n-1인 정수형 2차원 배열
from collections import deque, defaultdict

def bfs(graph, start, visited):
    cnt = 1 # 시작한 노드는 연결된 노드가 1개로 시작됨
    d = deque([start])
    visited[start] = 1    
    while d:
        b = d.popleft()
        for i in graph[b]:
            if not visited[i]:
                d.append(i)
                visited[i] = 1
                cnt += 1
    return cnt

def solution(n, wires):
    wire = deque(wires) # 전선을 하나씩 끊어 탐색해야하므로 deque 사용
    res = n # n 변경하지 않기 위해
    for _ in range(len(wires)):
        a = wire.popleft()
        visited = [0] * (n+1)
        graph = defaultdict(list)
        cnt_li = [] # 전선을 끊어서 나온 전력망 두개의 각각 송전탑 개수 저장 리스트
        for v1, v2 in wire:
            graph[v1].append(v2)
            graph[v2].append(v1)
        for i in range(1, n+1):
            if not visited[i]:
                cnt_li.append(bfs(graph, i, visited))
        res = min(abs(cnt_li[0] - cnt_li[1]), res)
        wire.append(a) # 다른 전선 끊기 위해 끊었던 전선 다시 붙여줌
    return res