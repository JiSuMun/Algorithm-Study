def solution(clothes):
    d = {}
    answer = 1
    for i in clothes:
        d[i[1]] = d.get(i[1],1)+1          
        # 옷 종류가 추가 될때마다 옷 가짓수 +1, 안입는 경우도 있느니 시작은 1
    for value in d.values():
        answer *=value                     
        # 조합
    return answer-1                        
    # 모두 안입는경우를 빼기

# 시간복잡도는 for문 순회 O(n)