# Programmers 스택/큐 2. 기능개발

# 시간복잡도: O(N)
import math

def solution(progresses, speeds):
    days = []
    answer = []
    
    for i in range(len(progresses)):
        take_time = math.ceil((100 - progresses[i]) / speeds[i])
        
        if i == 0:
            days.append(take_time)
        else:
            if take_time <= days[0]:
                days.append(take_time)
            else:
                answer.append(len(days))
                days.clear()
                days.append(take_time)
    else:
        answer.append(len(days))
                
    return answer

'''
1. 작업 소요 일수와 배포 개수를 저장할 빈 리스트를 각각 만든다.
2. 제일 첫 번째 작업의 '(100-작업 진도)/작업속도'를 올림한 값을 days(작업 소요 일수) 리스트에 넣는다.
3. 그다음 작업의 소요 일수와 비교하는데 해당 값이 리스트에 저장된 첫 번째 값보다 같거나 작다면 해당 값을 리스트에 추가한다.
4. 반대로 해당 값이 리스트에 저장된 첫 번째 값보다 크다면 리스트에 지금까지 저장되어 있던 요소의 개수를 센 값을 'answer' 리스트에 넣고 해당 리스트를 비운 뒤 작업 소요 일수를 저장한다.
5. 위 과정을 작업의 개수만큼 반복한다.
6. 반복이 끝난 후 days 리스트에 요소가 남아있는 요소의 길이를 answer 리스트에 추가하고 answer 값을 출력한다.
'''
