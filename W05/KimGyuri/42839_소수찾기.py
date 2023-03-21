# Programmers 완전탐색 3. 소수 찾기

# 시간복잡도: O(2^n * sqrt(max_num))

from itertools import permutations

def solution(numbers):
    answer = 0
    
    num_set = set()
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            num = int(''.join(j))
            num_set.add(num)
    
    for num in num_set:
        if num < 2:
            continue
        else:
            for n in range(2, num):
                if num % n == 0:
                    break
            else:
                answer += 1

    return answer

'''
1. permutations 함수를 사용하여 주어진 문자열 numbers로 만들 수 있는 모든 숫자 조합을 만든다.
2. 이 숫자 조합을 set에 넣어 중복 값을 제거한다.
3. set의 숫자를 하나씩 불러와 소수인지 확인하고 소수가 몇 개인지 출력한다.
'''
