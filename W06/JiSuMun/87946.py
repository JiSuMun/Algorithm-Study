# 완전탐색
# 피로도
# 시간복잡도: O(N! * N) => 시간 복잡도가 O(N!)인 dfs 함수를 호출하고 dfs 함수를 호출할 때마다 모든 요소를 ​​반복
"""
k => 현재 피로도
dungeons[i][0] => 최소 필요 피로도
dungeons[i][1] => 소모 피로도
NameError: not defined => global 사용
미리 visited를 len(dungeons) 사용해줬으나 NameError로 새로운 변수 사용해줌
permutations 사용하면 더 잘 풀수 있을 것 같음
"""

res = 0
visited = []
def solution(k, dungeons):
    global res, visited
    visited = [0] * len(dungeons)
    dfs(k, 0, dungeons)
    return res
def dfs(k, cnt, dungeons):
    global res   
    if cnt > res: res = cnt
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = 1
            dfs(k-dungeons[i][1], cnt+1, dungeons)
            visited[i] = 0 # 복구

# 신박한 풀이

solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])

"""
리스트 컴프리헨션에 든 for문의 변수를 보자면, i 는 d의 인덱스 값 / (m, u)는 d의 값. 즉 최소 피로도와 소모피로도다. 리스트 컴프리헨션의 각 요소는 k>m보다 클 때만 생성된다. 즉, 현재 피로도가 최소피로도보다 클 때만 생성된다. 근데 그 값이라는 것이 solution(k - u, d[:i] + d[i+1:]) + 1 이다. solution(총 피로도, 던전의 배열) 함수에 현재 피로도-소모피로도를 다시 총피로도라는 매개변수로 넣어주고, 던전의 배열이라는 매개변수에는 던전의 i번째 던전을 제거한 모든 던전의 배열을 다시 집어 넣는다. 그리고 1을 더한 것. solution이라는 함수 자체가 저 값과 0 중에 큰 것을 리턴하는데, 저 값이라는 것에 solution이 들어 있으니 아마도 재귀함수 같다.
"""