def solution(sizes):
    x=0; y=0
    for a,b in sizes:
        t1 = max(a,b)
        t2 = min(a,b)
        x = max(t1,x)
        y = max(t2,y)
    answer = x*y
    return answer

#시간복잡도는 a,b의 sizes 만큼의 순회 O(N)