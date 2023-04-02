# 12906
# 시간 복잡도: O(N)
def solution(arr):
    answer = []
    
    for i in range(len(arr)):   # 입력 리스트의 길이만큼의 for문 생성
        if i == 0:              # 만약 첫번째 i가 0이면
            answer.append(arr[i])   # answer에 arr의 i번째 요소를 추가한다.
        elif arr[i] != arr[i-1]:    # 그게 아니라 arr의 i번째 요소와 arr의 i-1번째 요소가 같지 않다면
            answer.append(arr[i])   # # answer에 arr의 i번째 요소를 추가한다.
    
    return answer # answer 반환