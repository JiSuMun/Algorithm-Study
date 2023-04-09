def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    global root
    root = {v:v for v in range(n)}
    link = 0
    while link < n-1:   
        for v1, v2, cost in costs:
            if get_root(v1) == get_root(v2):
                continue
            else:
                root[get_root(v2)] = get_root(v1)
                answer += cost
                link += 1
    return answer

def get_root(v):
    global root
    if root[v] == v:
        return v
    else:
        return get_root(root[v])
    

# 크루스칼 알고리즘
# 초기에는 모든 정점들이 서로 독립된 집합으로 존재합니다. 간선들을 가중치의 오름차순으로 정렬한 후, 가장 작은 가중치의 간선부터 연결합니다. 이 때, 연결하려는 두 정점이 서로 다른 집합에 속해 있다면, 이 간선을 추가하고 두 정점이 속한 집합을 하나로 합칩니다. 이 과정을 모든 정점이 연결될 때까지 반복합니다.
# Union-Find 자료구조를 사용하여 구현하면 효율적
# Kruskal 알고리즘의 시간 복잡도는 간선의 수를 m, 정점의 수를 n이라고 할 때, 정렬하는 데 O(mlogm) 시간이 소요되며, 간선을 추가하면서 집합을 합치는 과정에서 최대 O(mlogn) 시간이 소요됩니다. 따라서 전체 시간 복잡도는 O(mlogm)이 됩니다.

n, costs = 4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]] # return = 4
print(solution(n, costs))