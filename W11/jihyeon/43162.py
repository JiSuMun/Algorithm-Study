# 43162 (네트워크)
# 시간 복잡도: O(n^2) - 이유는 DFS 함수 내에서 for문이 두 번 중첩되어 있기 때문입니다. DFS 함수는 각각의 컴퓨터를 한 번씩 방문하며, 방문한 컴퓨터와 연결된 다른 컴퓨터를 차례로 방문하며 더 깊이 들어가는 과정을 거칩니다. 이때 각 컴퓨터와 연결된 모든 다른 컴퓨터를 방문해야 하므로, 연결된 컴퓨터의 개수에 비례하는 for문이 내부에 중첩되어 있습니다.


# DFS 활용
def solution(n, computers):
    cnt = 0
    visited = [False for i in range(n)]

    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            cnt += 1    # DFS로 최대한 많은 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크가 된다
    return cnt

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1: # 연결된 컴퓨터
            if visited[connect] == False:
                DFS(n, computers, connect, visited)



# 백준에서 비슷한 문제를 본 경험이 있어 어렵지 않게 풀 수 있을 줄 알았지만 막상 코드로 구현하려니 생각보다 어려웠다.
# dfs에서 재귀적인 방식으로 구현을 했는데, 아직까진 재귀적인 코드 구현이 미숙한 것 같다.
