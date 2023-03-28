# 84512 (모음사전)
# 시간복잡도: O(5^5) - 문자열의 길이가 최대 5이므로, 5개의 모음 중 하나를 선택하는 경우의 수는 최대 5^5개

from itertools import product

def solution(word):
    wlist = []

    for i in range(1, 6):
        for j in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            wlist.append(''.join(list(j)))

    wlist.sort()
    return wlist.index(word) + 1

# word 리스트 길이가 5밖에 되지 않기 때문에 중복 순열을 이용해 가능한 모든 조합을 구하고 index를 찾음
# product : 데카르트 곱, 중첩된 for 루프와 동등한 역할
