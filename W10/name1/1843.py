# 1843 (사칙연산)
# 시간 복잡도: O(N) - 주어진 리스트 arr 을 한번 순회하는 for 문이 있으며, 이 때 arr 을 순회하는 횟수는 arr 의 길이 N 입니다. 따라서 시간 복잡도는 O(N) 입니다.

def solution(arr):
    minmax = [0, 0]
    sum_value = 0

    for idx in range(len(arr)-1, -1, -1):
        if arr[idx] == '+':
            continue

        elif arr[idx] == '-':
            tempmin, tempmax = minmax
            minmax[0] = min(-(sum_value + tempmax), -sum_value+tempmin)
            # -(sum + max):-가 식 전체에 붙는 경우, -sum+min: -가 이전 -값 앞까지만 붙는 경우

            minus_v = int(arr[idx+1])
            minmax[1] = max(-(sum_value+tempmin), -minus_v+(sum_value-minus_v)+tempmax)
            # -(sum + min):-가 식 전체에 붙는 경우, -v+(sum-v)+max: -가 바로 뒤의 값에만 붙는 경우

            sum_value = 0

        elif int(arr[idx]) >= 0:
            sum_value += int(arr[idx])

    minmax[1] += sum_value


    return minmax[1]


# 식을 뒤에서 부터 읽으며 -를 만났을 때에는 최댓값과 최솟값을 갱신하고 +를 만나면 이전 -부터 다음 -까지 숫자를 더해 식을 계산해나가는 방식

# 문제 풀이 방법이 잘 생각나지 않아 다른 분의 풀이를 참고하여 풀었지만 
# 풀이를 본 후에도 개인적으로 이해가 잘 가지 않는 문제

