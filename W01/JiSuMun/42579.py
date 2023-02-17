# 해시
# 베스트앨범
# 시간복잡도: 이중 for문 O(N^2), sorted  O(NlogN) => O(N^2)
def solution(genres, plays):
    res = []
    d1 = {}
    d2 = {}
    # 고유번호, 장르, 재생횟수
    for i, (j, l) in enumerate(zip(genres, plays)):
        if j not in d1: d1[j] = [(i, l)]
        else: d1[j].append((i, l))
        
        if j not in d2: d2[j] = l
        else: d2[j] += l
    for k, v in sorted(d2.items(), key = lambda x: x[1], reverse = True):
        for (i, l) in sorted(d1[k], key = lambda x: x[1], reverse = True)[:2]:
            res.append(i)
    return res

"""
enumerate(): 인덱스와 원소로 이루어진 튜플 만들어줌
d1: {장르: [(고유번호, 재생횟수)]}
d2: {장르: 재생횟수}
속한 노래가 많이 재생된 장르를 먼저 수록 => d2 재생횟수 기준 정렬 [('pop', 3100), ('classic', 1450)] => 'pop'부터 출력되게끔
장르 내에서 많이 재생된 노래를 먼저 수록 => d1 재생횟수 기준 정렬 => 고유번호 리스트 추가
pop: [(4, 2500), (1, 600)], classic: [(3, 800), (0, 500)]
[:2] : 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시 => 2개만 필요
"""