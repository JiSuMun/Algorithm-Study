def solution(arr):
    
    """
    알고리즘 : 
    최대 = 최대 + 최대, 최대 - 최소
    최소 = 최소 + 최소, 최소 - 최대
    """

    # dummy 최대, 최소 값
    INF = int(10e6)
    NINF = int(-10e6)
   
    # 연산자와 숫자를 분리
    numbers = []
    operations = []
    for char in arr:
        if char in "+-":
            operations.append(char)
        else:
            numbers.append(int(char))
    
    # 연산 결과를 캐싱할 DP 행렬
    n = len(numbers)
    dp_max = [[NINF]*n for _ in range(n)]
    dp_min = [[INF]*n for _ in range(n)]

    # 최댓값 구하기
    def get_max(i, j):

        answer = dp_max[i][j]

        # 이미 저장된 값이 있으면 사용
        if answer > NINF:
            return answer
        
        # 단일 숫자인 경우 숫자 return 
        if i == j:
            answer = dp_max[i][j] = numbers[i]
            return answer
        
        # 최댓값 구하기
        for k in range(i, j):
            f = operations[k]
            if f == "+":
                dp_max[i][j] = max(dp_max[i][j], get_max(i, k) + get_max(k+1, j))
            else:
                dp_max[i][j] = max(dp_max[i][j], get_max(i, k) - get_min(k+1, j))

        answer = dp_max[i][j]
        return answer

    # 최솟값 구하기 
    def get_min(i, j):

        answer = dp_min[i][j]

        if answer < INF:
            return answer
        
        if i == j:
            answer = dp_min[i][j] = numbers[i]
            return answer
        
        for k in range(i, j):
            f = operations[k]
            if f == "+":
                dp_min[i][j] = min(dp_min[i][j], get_min(i, k) + get_min(k+1, j))
            else:
                dp_min[i][j] = min(dp_min[i][j], get_min(i, k) - get_max(k+1, j))

        answer = dp_min[i][j]
        return answer
    
    # 전체 식의 최댓값   
    answer = get_max(0, n-1)
    return answer


arr, result = ["1", "-", "3", "+", "5", "-", "8"], 1
print(solution(arr), result)
arr, result = ["5", "-", "3", "+", "1", "+", "2", "-", "4"], 3
print(solution(arr), result)


# 소요시간 : 64 min
# 시간복잡도 : O(n^3)


# 시간복잡도 분석 feat. chatGPT
# 이 코드는 주어진 수식에서 최대값과 최소값을 찾기 위한 동적 프로그래밍(Dynamic Programming) 방식을 사용한 파이썬 함수입니다. 시간복잡도는 O(n^3)입니다.

# 함수의 개요:
# 입력된 수식(arr)을 숫자와 연산자로 분리합니다.
# dp_max와 dp_min을 초기화합니다. dp_max[i][j]는 i부터 j까지의 숫자와 연산자들로 구성된 수식의 최대값을 나타내고, dp_min[i][j]는 최소값을 나타냅니다.
# get_max와 get_min 함수를 정의합니다. 이 함수들은 각각 주어진 범위의 최대값과 최소값을 찾는 역할을 합니다.
# 모든 가능한 연산 순서를 고려하여 최대값과 최소값을 찾습니다. 이 과정에서 동적 프로그래밍을 사용하여 중복되는 부분문제를 효율적으로 계산합니다.
# get_max(0, n-1)을 호출하여 최종적인 최대값을 계산한 후 반환합니다.
# 시간복잡도 분석:

# get_max와 get_min 함수는 각각 O(n^2)의 시간복잡도를 가집니다. 함수 내부의 for문이 n번 반복되고, 각 반복에서 최대 n번의 재귀 호출이 발생합니다.
# get_max와 get_min 함수가 서로 호출되는 상호 재귀(mutual recursion) 구조 때문에, 실제 시간복잡도는 O(n^3)가 됩니다.
# 따라서 이 함수의 시간복잡도는 O(n^3)입니다.