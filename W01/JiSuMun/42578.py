# 해시
# 위장
# 시간복잡도: for문 => O(N)
def solution(clothes):
    c = {}
    for k, v in clothes:
        c[v] = c.get(v, 0) + 1
    res = 1
    for i in c:
        res *= (c[i] + 1)
    return res - 1
"""
옷 종류와 개수 딕셔너리로 만들기
.get(key, 0): 해당하는 value가 있으면 가져오고, 아닐 경우 0 디폴트값으로 지정
옷 종류별 경우의 수 res 곱셈 (+1은 아무것도 입지 않은 경우가 포함)
결과에서 무조건 하나는 입어야 하므로 1빼줌
"""