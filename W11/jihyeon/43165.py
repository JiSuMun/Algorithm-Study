# 43165 (타겟 넘버)
# 시간 복잡도: O(2^n) - 이유는 모든 경우의 수를 탐색해야 하기 때문입니다. numbers의 길이가 n이면, 더하거나 빼는 경우의 수가 2가지이므로, 최종적으로 계산해야 할 경우의 수는 2^n개가 됩니다.


# BFS를 활용한 풀이
def solution(numbers, target):
    result = [0]          # 모든 계산 결과 담는 곳     
    cnt = 0 

    for num in numbers : 
        temp = []

        # 자손 노드 
        for i in result : 
            temp.append(i + num)    # 더하는 경우 
            temp.append(i - num)    # 빼는 경우 

        result = temp 

    # 모든 경우의 수 계산 후 target과 같은지 확인 
    for j in result : 
        if j == target : 
            cnt += 1

    return cnt
