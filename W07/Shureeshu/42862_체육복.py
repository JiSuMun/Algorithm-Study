# 42862_체육복

# n 전체 학생의 수
# lost 체육복을 도난당한 학생들의 번호가 담긴 배열
# reserve 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열
# return 체육수업을 들을 수 있는 학생의 최댓값
def solution(n, lost, reserve):
    answer = n
    # 학생들의 상태 초기화
    status = [1]*(n+2)
    
    # 예비 체육복이 있는 학생들
    for student in reserve:
        status[student] += 1
        
    # 체육복을 잃어버린 학생들
    for student in lost:
        status[student] -= 1
    
    # 앞번호 학생부터 탐색
    for i in range(1, n+1):
        # 빌려 주기 가능할 때 - 뒷번호 학생이 필요하면 빌려준다.
        if status[i] == 2:
            if status[i+1] == 0:
                status[i+1] = 1
                i += 1
        # 체육복 없을 때, 뒷번호 학생이 빌려줄 수 있는지 탐색
        elif status[i] == 0: 
            if status[i+1] == 2:
                status[i+1] = 1
                i += 1
            else:
               # 체육수업 참여 불가 
                answer -= 1
            
    return answer


# 이 코드의 시간 복잡도는 O(n log n)입니다. 
# 이 코드는 n 번의 반복문을 실행합니다. 각 반복마다, 상수 시간 내에 체육복을 빌리거나 빌려줄 수 있도록 상태를 업데이트하는 몇 가지 작업을 수행합니다. 
# 전체적인 시간 복잡도는 O(n)이 됩니다. 
# 하지만, 반복문 내에서 i 변수가 추가로 증가되는 경우가 있습니다. 이러한 경우, 반복문이 종료될 때까지 반복되는 추가 작업이 필요하므로, 시간 복잡도가 O(n log n)으로 증가합니다. 
# 따라서, 최악의 경우, 이 코드는 O(n log n) 시간 복잡도를 가집니다.