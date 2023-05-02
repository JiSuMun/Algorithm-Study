# Programmers 깊이/너비 우선 탐색(DFS/BFS) 4. 단어 변환

# 시간복잡도: O(N^2)
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque()
    queue.append([begin, 0])

    while queue:
        current_word, cnt = queue.popleft()

        if current_word == target:
            return cnt

        for i in range(len(words)):
            temp = 0
            compare_word = words[i]
            for j in range(len(current_word)):
                if current_word[j] != compare_word[j]:
                    temp += 1
            if temp == 1:
                queue.append([compare_word, cnt + 1])
    return 0

'''
1. target 단어가 words 리스트 안에 없으면 변환할 수 없으므로 -1을 반환한다.
2. 맨 처음 begin 단어와 cnt 0 값을 초깃값으로 설정한다.
3. 그리고 words 리스트 속 단어들과 비교해 나간다. 한 번에 한 개의 알파벳만 바꿀 수 있기 때문에 알파벳이 하나만 다른 단어를 덱에 넣는다.
4. 3번 과정을 반복하며 단계별로 변환한 단어가 target 단어와 같은지 비교한다. 같다면 몇 단계를 거쳤는데 카운트 횟수를 반환한다. 위 과정이 모두 끝났음에도 변환할 수 없는 경우에는 0을 반환한다.
'''