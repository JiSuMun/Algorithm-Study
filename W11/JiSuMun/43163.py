# 깊이/너비 우선 탐색(DFS/BFS)
# 단어 변환
# 시간복잡도: O(N^2 * M) N은 단어의 길이, M은 단어의 개수
"""
백준이나 swea에서 분명 푼 적 있는 문제 유형

1. 두 개의 단어 begin, target과 단어의 집합 words

2. begin에서 target으로 변환하는 가장 짧은 변환 과정

3. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.

4. words에 있는 단어로만 변환할 수 있습니다.

5. 각 단어는 알파벳 소문자로만 이루어져 있습니다.

6. 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.

7. words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.

8. begin과 target은 같지 않습니다.

9. 변환할 수 없는 경우에는 0를 return

최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return
"""
from collections import deque
def solution(begin, target, words):
    if target not in words: return 0
    n = len(begin)
    graph = {}
    words.append(begin)
    for word in words:
        graph[word] = []
        for w in words:
            if word == w: continue
            cnt = 0
            for i in range(n):
                if word[i] != w[i]: cnt += 1
                if cnt > 1: break
            if cnt == 1: graph[word].append(w)
    d = deque([(begin, 0)])
    visited = set()
    while d:
        cur, change = d.popleft()
        if cur == target: return change
        for next in graph[cur]:
            if next not in visited:
                visited.add(next)
                d.append((next, change+1))
    return 0

"""
제일 처음 words에 target이 없으면 미리 0을 return하여 시간 줄임
단어의 알파벳개수에 따라서 한 글자만 다를 경우 연결
bfs 이용함
words에 begin을 넣어주는 이유는 words에 넣어야 begin을 뜯어서 한글자만 차이나는 단어를 찾는 과정을 줄일 수 있기 때문
"""