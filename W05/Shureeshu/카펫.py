# 제한사항
# 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
# 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

def solution(brown, yellow): # O(N)
    for width in range(brown//2, 2, -1):
        height = brown//2 - width + 2
        if yellow == (height-2)*(width-2):
            return [width, height]
        
# 1. brown으로부터 가능한 카펫의 가로길이와 세로길이의 조합을 구한다.
# 2. yellow의 갯수와 모순이 있는지 체크해보고 모순이 없다면 return 한다.