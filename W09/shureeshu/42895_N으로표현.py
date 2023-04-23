def solution(N, number):
    answer = -1
    numbers = { i:{int(str(N)*i), } for i in range(1, 9)}
    for i in range(1, 9):
        j = 1
        while j < i:
            A = list(product(numbers[j], numbers[i-j]))
            for x, y in product(numbers[j], numbers[i-j]):
                if y == 0:
                    numbers[i].update([x+y, x-y, x*y])
                else:
                    numbers[i].update([x+y, x-y, x*y, x//y])
            j += 1
        if number in numbers[i]:
            answer = i
            break
          
    return answer

from itertools import product

# 이 코드의 시간 복잡도를 분석하기 위해 주요 부분을 살펴보겠습니다.

# numbers 딕셔너리 초기화: numbers = {i: {int(str(N) * i),} for i in range(1, 9)}에서 numbers 딕셔너리를 초기화하는데 O(1) 시간이 걸립니다 (여기서 상수 8은 무시할 정도로 작습니다).

# 외부 for 루프: for i in range(1, 9): 루프에서 최대 8번 반복됩니다. 이 루프의 내부에서 다음 작업을 수행합니다.

# 내부 while 루프: while j < i: 루프는 최대 8번 반복됩니다.

# product(numbers[j], numbers[i-j])에 의해 생성되는 조합의 수는 최대 O(4^k)이며, k는 j와 i-j에 대한 N의 연산 횟수입니다.

# 이중 for 루프: for x, y in product(numbers[j], numbers[i-j]): 루프는 최대 O(4^k)번 반복됩니다. 이 루프 내에서 x와 y에 대한 사칙연산 결과를 numbers[i]에 추가하는 데 O(1) 시간이 걸립니다.

# 따라서 전체 시간 복잡도는 외부 for 루프의 반복 횟수와 내부 while 루프의 반복 횟수, 이중 for 루프의 반복 횟수를 곱한 값인 O(8 * 8 * 4^k)로 근사할 수 있습니다. 여기서 k는 최대 8입니다.

# 그러나 k가 높아질수록 product 함수에 의해 생성되는 조합의 수가 줄어들므로, 실제 시간 복잡도는 이론적인 최대치보다는 작을 것입니다. 그럼에도 불구하고, 이 알고리즘의 시간 복잡도는 입력 크기와 조합에 따라 크게 달라질 수 있습니다.


N,	number = 5,	12	# return 4
print(solution(N, number))
N,	number = 2,	11	# return 3
print(solution(N, number))