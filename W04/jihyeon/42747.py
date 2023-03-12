# 42747 (H-Index)
# 시간 복잡도: O(n log n)
def solution(citations):
    citations.sort(reverse=True)        # 인용 횟수 리스트 citations 내림차순 정렬
    for i, j in enumerate(citations):   # citations 리스트의 인덱스와 원소를 차례로 접근
        if i >= j:              # 만약 인덱스 i가 원소 j보다 크거나 같다면
            return i            # 인덱스 i 반환
    return len(citations)       # 원소 j보다 크거나 같은 인덱스 i가 없다면 citations 리스트의 길이 반환


# 개인적으로 문제 설명이 부족하다 느껴져 문제를 이해하기 어려웠다. 
# 그래서 h-index에 대해 따로 찾아보게 되었다.
# 문제를 이해한 후 쉽게 풀 수 있었던 것 같다.

