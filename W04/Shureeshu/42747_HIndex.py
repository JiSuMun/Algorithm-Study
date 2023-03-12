# 제한사항
# 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
# 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.


def solution(citations): # O(NlogN)
    n = len(citations)
    citations.sort() # [0, 1, 3, 5, 6]
    h = n
    while h > 0 and citations[-h] < h: # citations는 정렬되어 있으므로 citations[-h] 보다 크거나 같은 수는 h개 이상이다.
        h -= 1
    return h

citations = [3, 0, 6, 1, 5]
print(solution(citations)) # 3