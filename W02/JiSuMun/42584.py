# 주식가격
# 스택/큐
# 시간복잡도: 이중 for문 => O(N^2)
def solution(prices):
    res = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                res[i] += 1
            else:
                res[i] += 1
                break
    return res
"""
스택을 사용하지 않은 풀이
초를 저장할 리스트를 만들어줌
범위를 지정해서 각각 비교한 후 해당하는 초 리스트의 인덱스에 넣어줌
"""

# 시간복잡도: O(N)
# price의 길이를 n이라 할 때, for루프 내의 while루프이므로 최악은 while만 n번
# while문을 돌 때마다 스택에서 제거시키므로 전체 루프의 실행 횟수는 n을 초과하지 않음
def solution(prices):
    res = [0] * len(prices)
    stack = []
    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            a = stack.pop()
            res[a] = i - a # 결과_가격이 떨어지지 않은 시간 저장
        stack.append(i) # 증가하는 시간을 stack에 저장
    while stack:
        a = stack.pop()
        res[a] = len(prices) - a - 1
    return res

"""
사실 이 문제가 왜 스택/큐 파트에 있는지 의문
하지만 스택으로 풀면 효율성테스트에서 훨씬 낮은 시간 기록
res는 가격이 떨어지지 않은 결과 시간을 저장하는 리스트
stack은 증가하는 시간은 저장하는 리스트
가격이 떨어진 경우에는 스택에서 제거되기 때문에 비교하지 않아도 되어서 연산이 줄어듦
res[a] = len(prices) - a - 1 는 모든 결과값의 규칙
"""