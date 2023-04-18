# 43105 (정수 삼각형)
# 시간 복잡도: O(n^2)

def solution(triangle):

    for i in range(1, len(triangle)):   # i = 몇 번 째 줄인지
        for j in range(i+1):    # j = 줄 안에서 인덱스
            if j == 0:  # 가장 왼쪽인 경우
                triangle[i][j] += triangle[i-1][j]
            elif j == i:    # 가장 오른쪽인 경우
                triangle[i][j] += triangle[i-1][-1]
            else:   # 가운데인 경우
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
                
    return max(triangle[-1])


# 반복문을 통해 한 줄씩 옮겨가며 최댓값이 될 수 있도록 값을 업데이트 해준다.
# 가장 왼쪽 혹은 오른쪽인 경우, 값을 비교할 필요가 없기 때문에 그 전 줄의 양쪽 끝 값을 더해주면 된다.
# 가운데인 경우 그 전줄의 두 값을 비교해 더 큰 값을 더해준다.