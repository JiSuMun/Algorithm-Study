# 제한사항
# sizes의 길이는 1 이상 10,000 이하입니다.
# sizes의 원소는 [w, h] 형식입니다.
# w는 명함의 가로 길이를 나타냅니다.
# h는 명함의 세로 길이를 나타냅니다.
# w와 h는 1 이상 1,000 이하인 자연수입니다.

# O(N)
def solution(sizes):
    answer = 0
    max_width = max([max(w, h) for [w, h] in sizes])
    max_height = max([min(w,h) for [w, h] in sizes])
    answer = max_width * max_height
    return answer

# 1 : 모든 명함의 가로길이, 세로길이 중 가장 긴 길이를 구한다.
# 2 : 모든 명함의 각 명함의 가로길이, 세로길이 중 짧은 쪽의 길이 중 가장 긴 길이를 구한다. 