# a = [5,5,1,5,5]

def solution(citations):
    a = max(citations)
    l = sorted(citations,reverse=True)
    for i in range(a,-1,-1):
        cnt = 0
        for j in l:
            if i<=j:
                cnt+=1
            else:
                break
        if cnt>=i:
            answer = i
            break
    return answer

# print(solution(a))
# 시간복잡도는 n번의 i값에서 j값과 n번 비교 따라서 O(N^2)