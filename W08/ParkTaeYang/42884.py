
def solution(routes):
    answer = 0
    c = - 30001
    routes = sorted(routes, key=lambda x: (x[1], x[0]))
    for i in routes:
        if i[0] <= c <= i[1]:
            continue
        else:
            c = i[1]
            answer +=1
    
    return answer