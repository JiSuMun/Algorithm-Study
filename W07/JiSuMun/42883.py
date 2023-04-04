# 탐욕법(Greedy)
# 큰 수 만들기
# 시간복잡도: O(N)
"""
for 루프를 반복하면서, 각 자릿수를 결과 문자열에 추가하고, 결과 문자열에서 숫자를 제거할 때마다 while 루프를 수행하기 때문 => O(N)
"""
"""
예시에서의 k개의 수를 제거했을 때 얻을 수 있는 숫자 리스트를 보면
'숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다.' 라고 되어있다.
이는 주어진 숫자에서 뒤에 존재하는 숫자는 숫자를 만들때 앞자리에 올 수 없다는 것을 뜻한다.

이때문에, k가 0이 될 때까지, 결과문자열이 공백이 아니면서 결과문자열의 마지막 숫자가 반복문을 순회 중 현재 숫자보다 작을때만, 결과문자열의 마지막 숫자를 제거해나가면 된다.

또한, 조건을 만족하지 못한다면 결과문자열에 하나씩 추가하며 반복문을 수행하게 된다.
"""

def solution(number, k):
    answer = ''
    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer = answer[:-1]
            k -= 1
        answer += i
    return answer[:-k] if k > 0 else answer


# number는 2자리 이상, 1,000,000자리 이하인 숫자입니다. => 시간초과
from itertools import combinations
def solution(number, k):
    answer = list(combinations(list(number), len(number)-k))
    return ''.join(sorted(answer, reverse=True)[0])