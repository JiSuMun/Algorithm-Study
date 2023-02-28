# 같은 숫자는 싫어
def solution(arr):
    answer = []
    for a in arr:
        if last(answer) == a:
            continue
        else:
            answer.append(a)
    return answer


def last(arr):
    if len(arr):
        return arr[-1]
    else:
        return -1
    
    