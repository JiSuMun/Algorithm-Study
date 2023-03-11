# 정렬
# H-Index
# 시간복잡도: sort => O(nlogn)
def solution(citations):
    citations.sort()
    for i, j in enumerate(citations):
        if j >= len(citations) - i: # h번 이상 인용된 논문이 h편 이상 
            return len(citations) - i # 이후의 값들은 남은 요소의 개수가 줄어들면서 더 이상 최댓값이 될 수 없음
    return 0

# 시간복잡도: sort => O(nlogn) 인 줄 알았으나, chatgpt결과 같은 sort를 사용했음에도 불구하고 O(N)이라고 나옴
def solution(citations):
    citations.sort(reverse=True)
    for i, j in enumerate(citations):
        if i >= j:
            return i
    return len(citations)
"""
위의 풀이가 아래의 풀이보다 시간면에서 아주 약간 효율적인 결과가 나왔음
"""