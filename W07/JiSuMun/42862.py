# 탐욕법(Greedy)
# 체육복
# 시간복잡도: O(N)
"""
1. 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
=> lost와 reserve에 동일하게 존재하는 값은 없애야 함.
=> 리스트 차집합은 set을 사용함

[set은 자료의 중복을 허용하지 않기 때문에, set을 이용하면 중복된 항목이 있는 리스트의 차집합을 빠르게 계산할 수 있습니다. 또한, set은 해시 테이블을 사용하여 내부적으로 구현되어 있어서 항목의 탐색과 추가/삭제 연산이 상수 시간에 이루어지므로, 리스트의 크기가 큰 경우에도 빠르게 처리할 수 있습니다.]

2. 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
=> 왼쪽 숫자부터 비교해야 함
"""
def solution(n, lost, reserve):
    s_reserve = set(reserve) - set(lost)
    s_lost = set(lost) - set(reserve)
    for i in s_reserve:
        if i-1 in s_lost: s_lost.remove(i-1)
        elif i+1 in s_lost: s_lost.remove(i+1)
    return n - len(s_lost)

"""
reserve와 lost 리스트 이름을 차집합 변수명으로 사용했는데, 문제가 틀렸다고 해서 이름만 바꿔주었더니 통과됨
"""