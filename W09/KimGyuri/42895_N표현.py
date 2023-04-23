# Programmers 동적계획법(Dynamic Programming) 1. N으로 표현

# 시간복잡도: O(N^2 * 2^N)
def solution(N, number):
    num = [set() for _ in range(9)]

    for i in range(1, 9):
        num[i].add(int(str(N) * i))
        for j in range(1, i):
            for k in num[j]:
                for l in num[i - j]:
                    num[i].add(k+l)
                    num[i].add(abs(k-l))
                    num[i].add(k*l)
                    if k != 0 :
                        num[i].add(l // k)
                    if l != 0 :
                        num[i].add(k // l)
        
        if number in num[i]:
            return i
    
    return -1

'''
1. 주어진 숫자 N은 최대 8번 사용할 수 있다. set을 만들되 인덱스 값을 설정할 때 편의를 위해 총 9개의 set을 만든다.
2. 가장 먼저 N을 N 사용횟수만큼 이어붙여 만든 수를 set에 넣는다. 그리고 N 사용횟수를 만족하는 조합으로 만들 수 있는 모든 수를 set에 넣는다.
    가령, N을 3번 사용한다면 N을 1번 사용해 만들 수 있는 수와 2번 사용해 만들 수 있는 수끼리 조합하여 사칙연산을 통해 만든 모든 수를 3번 set에 넣는다.
3. 2번에서 만든 set에 표현하고자 했던 number가 있으면 N 사용횟수를 출력한다.
'''