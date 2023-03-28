# 86971 (전력망을 둘로 나누기)
# 시간 복잡도: O(n^2) - 입력 크기인 노드 수(n) 만큼 for문이 돌며 각각의 노드를 시작점으로 bfs를 수행하기 때문 / 최악의 경우 모든 노드와 간선을 다 확인하므로 O(n^2 * (n+m))

from collections import deque

def bfs(start,visitied,graph):
    queue = deque([start])
    result = 1
    visitied[start] = True

    while queue:
        now = queue.popleft()
        
        for i in graph[now]:
            if visitied[i] == False:
                result += 1
                queue.append(i)
                visitied[i] = True
                
    return result
        

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
            
    for start,not_visit in wires:
        visitied = [False]*(n+1)
        visitied[not_visit] = True
        result = bfs(start,visitied,graph)
        if abs(result - (n-result)) < answer:
            answer = abs(result - (n-result))
        
    return answer


# 전선을 하나씩 끊어보고, 한 쪽만 bfs로 탐색하며 한 쪽 전력망에 속한 송전탐의 개수를 세고 남은 송전탑들과 얼마나 차이나는지 비교하는 코드

# 문제 풀이 방법을 생각하다 도저히 생각이 안나 결국 다른 분의 코드를 참고하여 풀었다.
# 그런데 역시 bfs 관련 문제였고, 사실 풀이를 보고도 잘 이해가 되지 않는 상태ㅠ.. 이것으로 본인은 bfs, dfs에 확실히 취약하다는 것을 다시 한번 깨닫게 되었다...
# 개념을 확실히 잡고 추후에 문제를 한번 더 보고 풀어봐야 할 것 같다.
