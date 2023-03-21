# 86491 (최소직사각형)
# 시간 복잡도: O(n)
def solution(sizes):
    w = []  # 너비를 담을 리스트 w
    h = []  # 높이를 담을 리스트 h
    
    for i in sizes:
        if i[0] > i[1]:     # sizes 요소에서 첫번째 값이 두번째 값보다 크면
            w.append(i[0])  # 첫번째 값을 w에 추가
            h.append(i[1])  # 두번째 값을 h에 추가
        else:               # 두번째 값이 첫번째 값보다 크면
            w.append(i[1])  # 두번째 값을 w에 추가
            h.append(i[0])  # 첫번째 값을 h에 추가
    
    return max(w) * max(h)  # w와 h에서 각각 최댓값을 꺼내 곱한 값을 반환



# 쉽게 풀 수 있는 문제지만 너무 복잡하게 생각해 시간을 꽤 잡아먹은 문제다.
