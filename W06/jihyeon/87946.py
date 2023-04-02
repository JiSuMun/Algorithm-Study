# 87946 (피로도)
# 시간 복잡도 : O(n!) - 입력 크기인 던전 수의 팩토리얼에 비례. 순열을 이용하여 모든 경우의 수를 확인하므로, 입력 크기가 커질수록 계산 시간이 기하급수적으로 늘어남. 따라서 입력 크기가 큰 경우 다른 알고리즘을 고려해야 함.

from itertools import permutations

def solutions(k, dungeons):
    answer = 0

    # 순열을 이용한 풀이
    for i in permutations(dungeons, len(dungeons)):
        tired = k   # 현재 피로도 = tired
        cnt = 0     # 유저가 탐험할 수 있는 던전 수 cnt

        for need, spend in i:
            if tired >= need:       # 현재 피로도가 최소 필요 피료도보다 크거나 같으면
                tired -= spend      # 현재 피로도 -= 소모 피로도
                cnt += 1            # cnt += 1
        
        answer = max(answer, cnt)
    return answer

# 지난주에 permutations를 이용한 문제가 있어 이 문제 또한 응용하여 풀 수 있었다.
