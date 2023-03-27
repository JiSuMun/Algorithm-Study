# Programmers 완전탐색 4. 카펫

# (1) 틀린 문제 풀이
def solution(brown, yellow):
    carpet = brown + yellow
    tmp = 1

    while True:
        width = (yellow // tmp) + 2
        height = tmp + 2

        if carpet == width * height:
            break
        else:
            tmp += 1
    
    return [width, height]


# (2) 맞는 답
# 시간복잡도: O(N)
def solution(brown, yellow):
    carpet = brown + yellow

    for h in range(1, yellow + 1):
        if yellow % h == 0:
            w = yellow // h

            if h > w:
                break

            carpet_width = w + 2
            carpet_height = h + 2

            if carpet_width * carpet_height - yellow == brown:
                return [carpet_width, carpet_height]

'''
1. 노란색 격자수의 약수를 구한다.
2. 구한 약수를 노란색 면적의 높이로 설정하고 노란색 면적을 높이로 나누어 너비도 구한다.
3. 노란색 면적을 갈색 테두리가 1줄 감싸고 있기 때문에 전체 카펫의 너비와 너비는 노란색 너비와 높이에 각각 2를 더한 값이다.
3. 너비가 높이보다 크면서 전체 카펫의 크기에서 노란 면적을 뺐을 때 갈색 면적 값이 나오는 조건을 만족하는 전체 카펫의 너비와 높이를 출력한다.
'''
