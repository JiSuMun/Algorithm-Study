def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for i in reserve[:]:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
    for j in reserve[:]:
        if j-1 in lost:
            lost.remove(j-1)
        elif j+1 in lost:
            lost.remove(j+1)
        
    answer = n-len(lost)
    return answer

# 시간복잡도는 정렬 O(NlogN)

n = 4
l = [1,2,4]
r = [1,2,4]

print(solution(n,l,r))
