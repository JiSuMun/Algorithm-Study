# 완전탐색
# 소수 찾기
# 시간복잡도: O(len(numbers)! + n + a * √a)
# a: 중복제거한 순열의 개수
from itertools import permutations
def prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def solution(numbers):
    res = 0
    result = []
    for i in range(1, len(numbers) + 1):
        result.append(list(set(map(''.join, permutations(numbers, i)))))
    a = list(set(map(int, set(sum(result, [])))))
    
    for j in a:
        if prime(j) == True: res += 1
    return res

"""
최대 약수는 sqrt(n)이므로 sqrt(n)까지만 검사
i까지 모든 수를 검사해봐도 되지만, 효율을 위해 i의 제곱근(i의 최대약수)까지만 검사
어떤 자연수의 약수의 개수는 제곱근을 기준으로 대칭이기 때문
permutations(iterable, r): iterable의 요소들의 길이 r인 순열로 반환
sum으로 리스트 덧셈하여 합해줌
"""