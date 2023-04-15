# 동적계획법(Dynamic Programming)
# N으로 표현
# 시간복잡도: O(N^3) => N이 최대 9이므로 효율적
"""
N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값

1. 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시

2. 최솟값이 8보다 크면 -1을 return

- 중복 피하기 위해 set 사용
"""
def solution(N, number):
    n_set = [set() for _ in range(9)]
    
    for i in range(1, 9):
        n_set[i].add(int(str(N)*i))
    
    # 사용횟수
    for i in range(1, 9):
        # i를 나눠서 j번, i-j번 사용하는 수를 사칙연산
        for j in range(1, i):
            for x in n_set[j]:
                for y in n_set[i-j]:
                    n_set[i].add(x+y)
                    n_set[i].add(x-y)
                    n_set[i].add(x*y)
                    if y != 0:
                        n_set[i].add(x//y)
        if number in n_set[i]:
            return i
    return -1

"""
- 숫자 여러번 반복되도록 str로 바꾼다음 곱해서 set에 넣어줌
- i번 사용해서 만들수 있는 수를 사칙연산해줌
    - 나누기는 분모가 0이면 무한대이므로 분모가 0이 아니라는 조건을 더해줌
    - 나머지는 무시하므로 // 해줌
- for문 반복할 때 range(1, 9) 사용 : 최솟값이 8보다 크면 -1 리턴
"""