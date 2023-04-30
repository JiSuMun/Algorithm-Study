# Programmers 깊이/너비 우선 탐색(DFS/BFS) 1. 타겟 넘버

# 시간복잡도: O(2^n)
def solution(numbers, target):
    answer = 0
    stack = [(0, 0)]
    
    while stack:
        current_sum, current_index = stack.pop()
        if current_index == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            stack.append((current_sum + numbers[current_index], current_index + 1))
            stack.append((current_sum - numbers[current_index], current_index + 1))
            
    return answer

'''
1. 현재까지의 합, 현재 인덱스를 (0, 0)으로 맨 처음 설정한 뒤 스택에 넣는다.
2. 스택에서 하나씩 pop 하여 불러오며 해당 인덱스 위치에 해당하는 숫자가 만들 수 있는 모든 결과를 스택에 넣는다. 가령, 불러온 수가 4이고 현재까지의 합이 0이라면 4와 -4라는 결과를 만들 수 있다.
3. 2번 과정을 반복하며 인덱스값이 numbers 배열의 길이와 같아졌을 때 타겟 넘버와 합이 같은지 비교하여 같다면 카운트한다.
'''