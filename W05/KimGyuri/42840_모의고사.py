# Programmers 완전탐색 2. 모의고사

# 시간복잡도: O(N)

from collections import deque

def solution(answers):
    student_1 = deque([1, 2, 3, 4, 5])
    student_2 = deque([2, 1, 2, 3, 2, 4, 2, 5])
    student_3 = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    
    answer = []
    scores = [0, 0, 0]
    
    for i in answers:
        num_1 = student_1.popleft()
        if num_1 == i:
            scores[0] += 1
        student_1.append(num_1)

        num_2 = student_2.popleft()
        if num_2 == i:
            scores[1] += 1
        student_2.append(num_2)

        num_3 = student_3.popleft()
        if num_3 == i:
            scores[2] += 1
        student_3.append(num_3)

    for i in range(3):
        if scores[i] == max(scores):
            answer.append(i + 1)
            
    return answer

'''
1. 3명의 학생이 적는 답의 배열을 덱의 형태로 만든다.
2. 학생들의 답을 앞에서부터 하나씩 pop 해서 문제의 정답과 비교하여 맞을 경우 1점을 추가하고 다시 덱에 넣는다.
3. 이 과정을 문제의 수만큼 반복한 뒤 가장 높은 점수를 받은 학생의 번호를 출력한다.
'''
