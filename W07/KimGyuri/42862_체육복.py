# Programmers 탐욕법(Greedy) 1. 체육복

def solution(n, lost, reserve):
    lst = [0]

    for i in range(1, n + 1):
        lst.append(1)
        if i in lost:
            lst[i] -= 1
        if i in reserve:
            lst[i] += 1
    lst.append(0)


    for j in range(1, n + 1):
        if lst[j] == 0: 
            if lst[j - 1] == 2:
                lst[j] += 1
                lst[j - 1] -= 1
                continue
                
            elif lst[j + 1] == 2:
                lst[j] += 1
                lst[j + 1] -= 1
                continue
    
    answer = 0
    for k in lst:
        if k >= 1:
            answer += 1

    return answer

'''
1. 기본적으로 모든 학생이 1개의 체육복을 가지고 있다고 가정하고 lost에 학생의 번호가 있으면 1을 빼고, reserve에 학생 번호가 있으면 1을 더한다.
2. 인덱스 값을 사용할 때 편의성을 위해 리스트의 맨 앞과 뒤에 허수 0을 덧붙여놓는다.
3. 체육복이 없는 경우 앞번호 학생 또는 뒷번호 학생에게 여분의 체육복이 있으면 빌린다.
4. 그 후 전체 학생 리스트에서 체육복의 개수가 1 이상인 학생 수를 카운트한다.
'''