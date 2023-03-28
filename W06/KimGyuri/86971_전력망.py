# Programmers 완전탐색 6. 전력망을 둘로 나누기

# 시간복잡도: O(n^3)
from collections import deque

def solution(n, wires):    
    answer = 100

    for i in range(n-1):
        wire = wires[:i] + wires[i+1:]

        graph = [[] for _ in range(n + 1)]
        for a, b in wire:
            graph[a].append(b)
            graph[b].append(a)

        node = []
        for j in range(1, n + 1):
            visited = [False] * (n + 1)
            node_num = deque([j])
            visited[j] = True

            lst = []

            while node_num:
                num = node_num.popleft()
                lst.append(num)

                for k in graph[num]:
                    if not visited[k]:
                        node_num.append(k)
                        visited[k] = True
            node.append(visited.count(True))

        if max(node) - min(node) < answer:
            answer = max(node) - min(node)

    return answer

'''
1. 전선들 중 하나를 끊는 것이기 때문에 wires 리스트에서 하나씩 원소를 삭제해가며 모든 경우의 수를 확인한다.
2. wires 리스트의 한 요소를 삭제한 뒤 나머지 요소로 그래프를 만든다.
3. BFS 알고리즘을 통해 하나의 노드(송전탑)에 몇 개의 전선이 연결되어 있는지 구한다.
4. 그 후 두 전력망이 나눠 가지는 송전탑 개수의 차이를 구하여 answer라는 변수에 넣고 송전탑의 개수가 가능한 비슷한, 즉 가장 작은 answer 값을 구한다. 
'''
