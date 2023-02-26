# 해시
# 폰켓몬
# 시간복잡도: len(set) 비교 => O(len(set))
def solution(nums):
    pon = set(nums)
    if len(nums) / 2 > len(pon):
        return len(pon)
    else: return len(nums) / 2

"""
중복된 값들이 있음 => set을 이용해 중복되지 않은 폰켓몬의 종류 구함
len(nums)/2 : 골라야 하는 폰켓몬 수 가 중복되지 않은 개수보다 적으면
가지고 가는 개수의 최댓값만큼의 종류 선택가능
"""