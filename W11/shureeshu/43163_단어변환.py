def solution(begin, target, words):

    answer = dict() # 몇 번째 변환인지 기록 (최단거리)

    que = deque([])

    # target 이 words 안에 있는지 체크
    if target in words:
        answer[begin] = 0
        que.append(begin)

    # 검색 시작 (BFS)
    while que:

        current = que.popleft()
        
        for word in words:

            # 1 글자만 다른 단어 찾는다.
            if sum(1 for a, b in zip(list(current), list(word)) if a!=b) == 1:

                # 목적지 도착
                if word == target:
                    return answer[current] + 1
                
                # 경로에 추가
                if word not in answer.keys() or answer[word] > answer[current] + 1:
                    answer[word] = answer[current] + 1
                    que.append(word)
    
    # 검색이 끝났지만 경로를 찾지 못했을 때
    return 0   


from collections import deque

# 게임맵최단거리와 동일한 알고리즘 사용

begin, target, words, result = "hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"],	4
print(solution(begin, target, words), result)

