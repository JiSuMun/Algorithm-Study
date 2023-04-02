# 42584 (주식가격)
# 시간 복잡도: 2중 for문 - O(N^2)
def solution(prices):
    answer = [0] * len(prices)  # 0으로 이루어진 prices 길이 만큼의 answer 리스트 생성

    for i in range(len(prices)):    # 리스트 순회를 위해 2중 for문 생성
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:  # 만약 i초 시점의 가격보다 j초 시점의 가격이 더 크거나 같다면
                answer[i] += 1          # answer += 1
            else:                       # 그게 아니라 만약 i초 시점의 가격보다 j초 시점의 가격이 더 작다면
                answer[i] += 1          # answer += 1
                break                   # 더 이상 비교할 필요가 없으므로 break
    return answer                       # answer 반환


