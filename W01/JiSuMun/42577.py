# 해시
# 전화번호 목록
# 시간 복잡도: sorted => O(NlogN)
def solution(phone_book):
    res = True
    p = sorted(phone_book)
    for i in range(len(p)-1):
        if p[i] == p[i+1][:len(p[i])]:
            res = False
            break
    return res

"""
이중 for문을 사용하게 되면 시간복잡도가 O(N^2)이 된다.
그리고, p[i] in p[i+1]은 첫 시작 뿐만 아니라 중간에 포함되어도 False가 되므로,
짧은 순서로 정렬해서, 슬라이싱을 통해 비교했다.
"""