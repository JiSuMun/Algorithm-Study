# Programmers 정렬 3. H-index

# 시간복잡도: O(NlogN)

def solution(citations):
    citations.sort()
    answer = len(citations)

    while True:
        cnt = len([i for i in citations if i >= answer])
        if cnt >= answer:
            return answer
        else:
            answer -= 1

'''
1. 논문의 인용 횟수가 담긴 배열 citations를 정렬한다. (시간복잡도를 줄이기 위한 방법)
2. H-index는 인용된 횟수가 h번 이상인 논문이 h 편 이상인 수의 최댓값이므로 현재 본인이 발표한 논문의 수가 최댓값일 수밖에 없다.
3. 따라서 answer 변수에 논문의 수를 저장해놓는다.
4. 반복문을 돌리며 answer 값보다 인용 횟수가 큰 논문의 개수를 센다.
5. 논문의 개수가 answer보다 크거나 같다면 H-index에 해당하므로 해당 값을 return 한다.
6. 그 반대라면 answer 값을 1씩 줄여나가면 위 과정을 반복한다.
'''
