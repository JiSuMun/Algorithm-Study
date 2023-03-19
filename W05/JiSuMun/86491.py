# 완전탐색
# 최소직사각형
# 시간복잡도: O(N)
def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])
    return max(w) * max(h)

"""
w, h 리스트를 만든다.
for문을 돌면서 w, h 중 큰 값은 w리스트 작은 값은 h리스트
두 개의 리스트에서 가장 큰 값을 곱한 값이 답
"""