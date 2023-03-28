# 86971_전력망을 둘로 나누기

# 제한사항
# n은 2 이상 100 이하인 자연수입니다.
# wires는 길이가 n-1인 정수형 2차원 배열입니다.
# wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.
# 1 ≤ v1 < v2 ≤ n 입니다.
# 전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.

# n :송전탑의 개수, 정점의 수 V = n
# wires :전선 정보, 간선의 수 E = len(wires)
# return :두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)
def solution(n, wires):
    answer = n
    # graph를 그린다. # O(E)
    graph = [[] for i in range(n+1)]
    for wire in wires:
        v1, v2 = wire
        graph[v1].append(v2)
        graph[v2].append(v1)
    # 해당 와이어 절단 시, 두 전력망이 가지고 있는 송전탑 개수의 차이를 구한다.
    for wire in wires:  # O(E * V * E)
        v1, v2 = wire
        # v1에 연결된 송전탑 개수 구하기, # O(V * E)
        # v2를 미리 방문 처리하고 DFS 한다.
        power_grid = set()
        visited = [False]*(n+1)
        stack = [v1]
        visited[v2] = True 
        while stack: 
            v1 = stack.pop()
            power_grid.add(v1)
            for v in graph[v1]:
                if not visited[v]:
                    stack.append(v)
            visited[v1] = True
        diff = n - len(power_grid) - len(power_grid)
        answer = min(answer, abs(diff))
    return answer

n, wires, result  = 9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]], 3
print(solution(n, wires))
n, wires, result  = 4, [[1,2],[2,3],[3,4]], 0
print(solution(n, wires))
n, wires, result  = 7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]], 1
print(solution(n, wires))

# 시간 복잡도 O(V * E^2)
# 1: 모든 와이어(간선)에 대해 해당 와이어 절단 시, 두 전력망이 가지고 있는 송전탑의 개수의 차이를 구한다. (완전 탐색)
# 2: 인접 리스트(graph)를 그린다.
# 3: 각 간선(와이어)에 대해, v2를 미리 방문 처리 한 후 DFS 하여, v1에 연결된 정점(송전탑)의 개수를 구한다.
# 4: answer 에는 diff 가 가장 작은 경우의 diff를 담는다.