# 완전탐색
# 카펫
# 시간복잡도: O(N)
def division(n):
    li = []
    for i in range(1, n//2+1):
        if n % i == 0: li.append(i)
    li.append(n)  
    return li

def solution(brown, yellow):
    n = brown + yellow
    k = division(n)
    for i in k:
        j = n // i
        if (j-2)*(i-2) == yellow: return [j, i]

"""
sqrt를 사용하여 제곱근을 만들어 trunc하여 비교하며 숫자를 조작하려고 했으나 실패
약수 리스트를 구하여 반복문을 돌림
너비와 높이, yellow와 관계가 있었다. => (너비-2)*(높이-2) = yellow
"""