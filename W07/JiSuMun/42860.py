# 탐욕법(Greedy)
# 조이스틱
# 시간복잡도: O(N)
"""
* 주의사항
!무조건 앞부터 시작하는 것이 아닌 마지막에서 시작할 수도 있다!

- 왼쪽시작만을 고려하여 처음에는 실패함

- 가장 최소로 이동할 수 있는 횟수는 name이 A로만 이루어진 경우로 name길이에서 1빼준 것

1. 현재 문자와 A 거리를 up, down으로 나누어 계산해줌 => up, down 중 어떤 것이 더 적게 이동할 수 있을 지 찾을 수 있음

2. A가 연속된 부분을 제외하여 왼쪽과 오른쪽 부분의 짧은 부분을 찾아야 하므로
=> next 변수에 다음 인덱스 저장하여 아직 마지막 글자가 아니거나 다음 글자가 A이면 인덱스 하나 더해줌

3. 최소 이동횟수 비교
    - 처음에 저장해놓은 m_move, 왼쪽 시작방식, 오른쪽 시작방식

    - 2*i => 현재 위치에서 왼쪽으로 이동한 거리
    - len(name)-next => 문자열 끝에서 남은 문자열 모두 탐색하기 위해 오른쪽으로 이동한 거리

    - i => 현재 위치에서 오른쪽으로 이동한 거리
    - 2*(len(name)-next) => 문자열 끝에서 남은 문자열 모두 왼쪽으로 이동한 거리
"""

def solution(name):
    answer = 0
    m_move = len(name) - 1
    for i, alpha in enumerate(name):
        up = ord(alpha) - ord('A')
        down = ord('Z') - ord(alpha) + 1
        answer += min(up, down)
        next = i+1
        while next < len(name) and name[next] == 'A':
            next += 1
        m_move = min(m_move, 2*i+len(name)-next, i+2*(len(name)-next))
    answer += m_move
    return answer