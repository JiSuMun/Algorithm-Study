# Programmers 해시 1. 폰켓몬

# 시간복잡도
# set: O(len(nums))
# 길이 확인: O(1)

def solution(nums):
    distinct = set(nums)
    answer = len(nums) // 2 if len(distinct) >= len(nums) // 2 else len(distinct)

    return answer

'''
set을 이용해 중복된 폰켓몬을 제거한 배열을 만든다.
기존의 폰켓몬 리스트 길이 N을 2로 나눈 값보다 set 길이보다 같거나 크다면 각각 모두 다른 종류의 N/2 마리의 폰켓몬을 가질 수 있다.
반면 기존의 폰켓몬 리스트 길이 N을 2로 나눈 값보다 set 길이가 작다면 선택할 수 있는 폰켓몬의 종류의 수는 set 길이 수라는 것이다.
'''
