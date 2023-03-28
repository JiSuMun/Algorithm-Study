# Programmers 완전탐색 7. 모음사전

# 시간복잡도: O(5^5 log 5^5)

from itertools import product

def solution(word):
    char = ['A', 'E', 'I', 'O', 'U']
    lst = []
    
    for i in range(1, 6):
        for j in product(char, repeat=i):
            lst.append(''.join(j))

    lst.sort()
    answer = lst.index(word) + 1

    return answer

'''
1. itertools의 product 함수를 이용해 1~5자리의 모든 글자 조합을 리스트에 담는다.
2. 리스트를 사전 순으로 정렬한 뒤 찾고자 하는 단어의 인덱스 값 + 1(인덱스는 0부터 시작하기 때문)을 출력한다.
'''
