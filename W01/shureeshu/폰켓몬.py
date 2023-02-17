# 폰켓몬
def solution1845(nums):
    N = len(nums)
    answer = min(N//2, len(set(nums)))
    return answer

