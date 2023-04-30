# 43163 (단어 변환)
# 시간 복잡도: O(N) - 여기서 N은 words 리스트의 단어 수입니다. 따라서 이 코드의 전체 시간 복잡도는 큐에 삽입되는 단어 수에 비례하게 됩니다.

from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append([begin, 0])    # [단어, 깊이]
    L = [0] * (len(words))    # 노드 방문 여부 확인 리스트

    while queue:
        word, cnt = queue.popleft()

        if word == target:
            answer = cnt
            break      

        for i in range(len(words)):
            temp_cnt = 0

            if not L[i]:    # 만약 확인하지 않은 단어라면
                # 추가로 그 단어가 words 속 단어와 다를 때 한 자씩 비교해서 더하기
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1

                if temp_cnt == 1:   # 만약 다른 글자 개수가 1개라면
                    queue.append([words[i], cnt+1])
                    L[i] = 1

    return answer


# 문제가 이해 안가서 결국 다른 사람의 풀이를 참조하였다.
# 그럼에도 개인적으로 이해가 잘 가지 않는 문제

