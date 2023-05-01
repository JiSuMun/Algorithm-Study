def solution(begin, target, words):
    answer = dict()
    que = deque([])
    if target in words:
        answer[begin] = 0
        que.append(begin)
    while que:
        current = que.popleft()
        for word in words:
            if sum(1 for a, b in zip(list(current), list(word)) if a!=b) == 1:
                if word == target:
                    return answer[current] + 1
                if word not in answer.keys() or answer[word] > answer[current] + 1:
                    answer[word] = answer[current] + 1
                    que.append(word)
    return 0   


from collections import deque


begin, target, words, result = "hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"],	4
print(solution(begin, target, words), result)