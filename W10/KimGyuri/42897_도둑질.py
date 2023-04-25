# Programmers 동적계획법(Dynamic Programming) 5. 도둑질

# 시간복잡도: O(n)
def solution(money):
    n = len(money)

    route_1 = [0] * n
    route_1[0] = money[0]
    route_1[1] = max(money[0], money[1])

    for i in range(2, n-1):
        route_1[i] = max(route_1[i-1], route_1[i-2] + money[i])

    route_2 = [0] * n
    route_2[0] = 0
    route_2[1] = money[1]

    for j in range(2, n):
        route_2[j] = max(route_2[j-1], route_2[j-2] + money[j])

    return max(max(route_1), max(route_2))
