def solution1(triangle):
    answer = triangle[0][0]
    if len(triangle) > 1:
        left_sub = []
        right_sub = []
    
        for row in triangle[1:]:
            left_sub.append(row[:-1])
            right_sub.append(row[1:])
        answer += max(solution(left_sub), solution(right_sub))
    return answer


def solution(triangle):
    row = triangle.pop()
    while True:
        if len(row) == 1:
            return sum(row)
        else:
            next_row = []
            for parent, left, right in zip(triangle[-1], row[:-1], row[1:]):
                next_row.append(parent + max(left, right))
            row = next_row
            triangle.pop()
                
# 아래에서 위로 탐색
# 각 단계에서 최대 값을 선택

# 시간 복잡도 : O(n^2), n = 삼각형의 높이

# 외부 while 루프: while True: 루프에서 최대 삼각형의 높이만큼 반복되며, 이 루프의 내부에서 다음 작업을 수행합니다.
# 내부 for 루프: for parent, left, right in zip(triangle[-1], row[:-1], row[1:]): 루프는 각 행의 요소 수만큼 반복됩니다. 삼각형의 높이가 n인 경우, i 번째 행에는 i 개의 요소가 있습니다 (1 <= i <= n). 따라서 각 행에서 O(i) 시간이 걸립니다.
# 외부 루프는 삼각형의 높이 n에 대해 내부 루프를 수행합니다. 내부 루프는 각 행의 요소 수에 따라 O(i) 시간이 걸리므로, 전체 시간 복잡도는 O(1 + 2 + 3 + ... + n)입니다. 이는 등차수열의 합으로 O(n*(n+1)/2) = O(n^2)로 근사할 수 있습니다.


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	# result 30
print(solution(triangle))

