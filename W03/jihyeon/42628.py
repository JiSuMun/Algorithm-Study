# 42628 (이중우선순위큐)
# 시간 복잡도: O(N^2logN) - 리스트의 길이가 N일 때, sort() 함수의 시간 복잡도인 O(NlogN)이 반복적으로 발생
def solution(operations):
    answer = []
    
    for i in operations:
        a, b = i.split()    # a에 I나 D를 저장 / b에 숫자 저장
        
        if a == 'I':        # 만약 a가 I라면
            answer.append(int(b))   # answer에 주어진 숫자 삽입
        else:               # 그게 아니라 a가 D라면
            if len(answer) > 0:     # 추가로 answer에 숫자가 삽입돼있는 상태라면
                if b == '1':        # 추가로 b가 1이라면
                    answer.pop()    # answer의 최댓값 삭제
                else:               # 그게 아니라 b가 -1 이라면
                    answer.pop(0)   # answer의 최솟값 삭제
            else:               # answer에 삽입된 숫자가 없다면                
                pass            # pass
        
        answer.sort()           # answer 정렬
        
    if len(answer) == 0:        # 만약 answer가 비어있다면
        return [0, 0]           # [0,0] 반환
    else:                       # 비어있지 않으면
        return [max(answer), min(answer)]   # answer의 최댓값, 최솟값 반환
    

# heap으로도 풀 수 있지만 배열을 이용해 풀어보았다.
# 시간 복잡도 면에서는 안좋은 풀이인 것 같다.

