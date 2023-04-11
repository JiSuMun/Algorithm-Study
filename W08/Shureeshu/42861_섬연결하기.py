
def solution(n, costs):
    answer = 0
    INF = int(10e6) # 연결할 수 없음을 나타내는 큰 수
    
    islands = set(range(n)) # 연결해야할 섬들의 목록
    
    graph = [[INF]*n for _ in range(n)] # 인접 행렬
    for v1, v2, cost in costs:
        graph[v1][v2] = cost
        graph[v2][v1] = cost
            

    v1 = 0
    while len(islands) > 1:
        # 모든 섬에는 최소 1개의 다리가 연결 되어 있어야한다.
        # 가능한 한 비용이 적은 다리로 연결 되는 것이 좋다.
        v2 = graph[v1].index(min(graph[v1]))
        answer += graph[v1][v2]
        
        # 두 섬을 연결하면 하나의 섬처럼 취급한다.
        graph.append([])
        for i in range(n):
            cost = min(graph[v1][i], graph[v2][i]) if i not in [v1, v2] else INF
            graph[i].append(cost)
            graph[-1].append(cost)
            graph[v1][i], graph[v2][i], graph[i][v1], graph[i][v2] = INF, INF, INF, INF
        graph[-1].append(INF)
        
        islands -= {v1, v2}
        new_v = n
        islands.add(new_v)
        v1 = new_v
        n += 1
        
            
    return answer


# 시간복잡도 : O(n^2)
# 그래프 생성: graph = [[INF]*n for _ in range(n)]에서 인접 행렬을 생성하는데 O(n^2) 시간이 걸립니다.
# 그래프 업데이트: for v1, v2, cost in costs: 루프에서 그래프를 업데이트하는데 O(m) 시간이 걸립니다. 여기서 m은 주어진 다리의 개수를 나타냅니다.
# 섬 연결: while len(islands) > 1: 루프에서 섬들을 연결하는 과정을 반복합니다. 이 루프는 n-1 번 반복됩니다.
# 그래프에서 최소 비용의 다리를 찾기 위해, graph[v1].index(min(graph[v1]))를 사용하여 O(n) 시간이 걸립니다.
# 그래프에 새로운 노드를 추가하고 업데이트하는 과정에서 O(n) 시간이 걸립니다.
# O(n^2) (그래프 생성) + O(m) (그래프 업데이트) + O(2n^2 - 2n) (섬 연결)

n, costs = 4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]] # return = 4
print(solution(n, costs))