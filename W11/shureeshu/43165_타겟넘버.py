def solution(numbers, target):
    if len(numbers) > 1:
        answer = solution(numbers[:-1], target+numbers[-1]) + solution(numbers[:-1], target-numbers[-1])
    else:
        if target + numbers[0] == 0 or target - numbers[0] == 0:
            return 1
        else:
            return 0
    return answer

# return 타겟 넘버를 만드는 방법의 수