# 완전탐색
# 모의고사
# 시간복잡도: O(N)
def solution(answers):
    a1, cnt1 = [1, 2, 3, 4, 5], 0
    a2, cnt2 = [2, 1, 2, 3, 2, 4, 2, 5], 0
    a3, cnt3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5], 0
    for i in range(len(answers)):
        idx1, idx2, idx3 = i%5, i%8, i%10
        if a1[idx1] == answers[i]: cnt1 += 1
        if a2[idx2] == answers[i]: cnt2 += 1
        if a3[idx3] == answers[i]: cnt3 += 1
    res = max(cnt1, cnt2, cnt3)
    result = []
    if res == cnt1: result.append(1)
    if res == cnt2: result.append(2)
    if res == cnt3: result.append(3)
    return result
"""
1, 2, 3번 수포자가 찍는 방식과 맞은 개수를 리스트와 cnt로 표현
answers 길이만큼 반복문돌림
인덱스를 각각 만들어 일치하다면 cnt 개수를 올림
가장 큰 값을 찾아 cnt와 일치하다면 가장 많이 맞은 사람이므로 result 리스트에 추가하여 반환
"""