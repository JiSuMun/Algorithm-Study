def solution(money):
    answer = 0

    n = len(money) # 마을의 집의 수
    dp = [0]*n # 연산 결과를 캐싱할 배열
    

    dp[0] = money[0] # 첫번째 집 털고 시작
    dp[1] = max(dp[0], money[1])
    for i in range(2, n-1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])

    answer = dp[-2]
    dp = [0]*n # 캐싱 초기화 

    dp[0] = 0 # 첫번째 집 안 털고 시작
    dp[1] = max(dp[0], money[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    
    answer = max(answer, dp[-1])

    return answer

"""
알고리즘:
첫번째 집을 털고 시작하는 경우와 안 털고 시작하는 경우 2가지를 구해 큰 결과를 return
"""

money, result = [1, 2, 3, 1], 	4
print(solution(money), result)


# 소요시간 : 20 min
# 시간복잡도 : O(n)

# 시간복잡도 분석 feat. chatGPT

# 첫 번째 집을 털고 시작하는 경우와 첫 번째 집을 털지 않고 시작하는 경우 두 가지를 계산하는 각각의 for문은 O(n)의 시간복잡도를 가집니다.
# 두 가지 경우를 각각 계산하므로 전체 시간복잡도는 2 * O(n)이지만, 상수는 고려하지 않으므로 결국 시간복잡도는 O(n)입니다.