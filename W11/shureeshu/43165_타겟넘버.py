
def solution(numbers, target):
    
    if len(numbers):
        # 주어진 숫자의 갯수가 1개 이상일 떄,
        # 재귀
        answer = solution(numbers[:-1], target+numbers[-1]) + solution(numbers[:-1], target-numbers[-1])
    
    else:

        if target == 0:
            # 완성
            return 1
        else:
            # 실패
            return 0
        
    return answer

# return 타겟 넘버를 만드는 방법의 수

# [4, 1, 2, 1], 4
# [4, 1, 2], 3    [4, 1, 2], 5    
# [4, 1], 1    [4, 1], 5    [4, 1], 7    [4, 1], 3
