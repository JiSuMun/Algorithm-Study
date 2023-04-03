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