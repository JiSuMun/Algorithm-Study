# 리스트
l = []
def solution(operations):
    for i in operations:
        if i[0] == 'I':
            l.append(int(i[2:]))
            l.sort()
        elif i == 'D 1':
            try:
                l.pop()
            except:
                continue
        else:
            try:
                l.pop(0)
            except:
                continue
    if l:
        answer = [max(l),min(l)]
    else:
        answer = [0,0]
    return answer

# ?
# 통과
# N번의 순환동안 최악의 경우 정렬만 N번하기 때문에 복잡도 (N^2logN)

#큐
# import queue
# que = queue.Queue()
# def solution(operations):
#     for i in operations:
#         if i[0] == 'l':             
#     answer = []

#     return answer




l2 = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]

