# 같은 숫자는 싫어
# 스택/큐
# 시간복잡도: for문 => O(N)
def solution(arr):
    res = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]: res.append(arr[i])
    return res

"""
i의 범위가 1부터 이므로 list의 0번인덱스를 미리 리스트에 추가해 놓음
"""