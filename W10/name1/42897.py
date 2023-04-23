# 42897 (도둑질)
# 시간 복잡도: O(n) - 주어진 금액 배열을 한 번 순회하면서 두 개의 배열을 각각 채우기 때문입니다. 따라서 이 함수는 금액 배열의 크기에 선형적으로 비례하여 작동합니다.

def solution(money):
    house1 = [0] * len(money)
    house2 = [0] * len(money)
    
    # 1번 집을 터는 경우
    house1[0] = money[0]
    for i in range(1, len(money) - 1):  # 마지막 집은 털지 못함
        house1[i] = max(house1[i - 1], house1[i - 2] + money[i])
    
    # 1번 집을 안터는 경우
    house1[0] = 0
    for i in range(1, len(money)):
        house2[i] = max(house2[i - 1], house2[i - 2] + money[i])

    return max(house1[-2], house2[-1])


# 1번 집을 털 경우 - 2번 집부터 마지막 바로 전 집까지 훔칠 수 있는 돈을 계산
# 1번 집을 털지 않을 경우 - 2번 집부터 마지막 집까지 훔칠 수 있는 돈을 계산
