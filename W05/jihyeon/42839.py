# 42839 (소수 찾기)
# 시간 복잡도: O(N! × N√N)
# 첫 번째 for 루프에서는 1부터 주어진 숫자의 길이까지 반복하며 각 숫자들을 조합하여 가능한 모든 순열을 만들어냅니다. 따라서 이 루프의 시간 복잡도는 O(N!)입니다.
# 두 번째 for 루프에서는 앞서 만든 모든 순열에 대해 소수인지 판별합니다. 이를 위해 각 숫자의 제곱근보다 작은 수까지 나눗셈을 진행하므로, 이 루프의 시간 복잡도는 O(N√N)입니다.
# 따라서 전체 함수의 시간 복잡도는 O(N! × N√N)입니다. 이는 매우 큰 시간 복잡도이므로, 숫자의 길이가 매우 큰 경우에는 실행 속도가 매우 느려질 수 있습니다. 이를 개선하기 위해서는, 불필요한 연산을 줄이거나 다른 알고리즘을 사용하는 것이 필요할 수 있습니다.

from itertools import permutations

def solution(numbers):
    answer = []     
    per = []                              
    num = [n for n in numbers]      #numbers를 하나씩 자른 것        

    for i in range(1, len(numbers)+1):      # numbers의 각 숫자들을 순열로 모든 경우의 수 만들기
        per += list(permutations(num, i))   # i개씩 순열 조합을 만듬

    new_num = [int(('').join(p)) for p in per]  # 각각의 순열 조합을 하나의 int형 숫자로 변환

    for n in new_num:       # new_num에 담은 숫자 각각이 소수인지 판별                  
        if n < 2:           # 만약 n이 2보다 작다면 (0, 1은 소수가 아니므로)
            continue        # 건너뜀

        check = True
        for i in range(2, int(n**0.5) + 1): # n의 제곱근보다 작은 수까지만 나눗셈
            if n % i == 0:                  # 하나라도 나눠떨어진다면 소수가 아님
                check = False
                break
            
        if check:
            answer.append(n)    # 만약 소수라면 리스트에 추가

    return len(set(answer))     # set으로 중복을 제거하고 답을 반환


# 숫자를 조합하는 방법을 모르겠어서 다른 분의 풀이를 참고하여 풀었다.
# permutations라는 것을 새로 알게 되었다.
# list(permutations(iterable, r)) : iterable에서 요소의 연속된 길이 r 순열을 반환한다.
# 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산해준다.

