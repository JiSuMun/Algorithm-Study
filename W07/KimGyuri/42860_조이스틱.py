# Programmers 탐욕법(Greedy) 2. 조이스틱

def solution(name):
    answer = 0
    
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    min_move = len(name) - 1
    for i in range(len(name)):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        min_move = min(min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next))

    answer += min_move
    
    return answer

'''
1. 상하로 움직여 주어진 알파벳 이름을 만드는 최솟값을 구한다.
1-1. A부터 특정 알파벳까지 움직였을 때의 횟수, 거꾸로 Z부터 움직였을 때의 횟수 중 최솟값을 구한다.

2. 좌우로 움직여 주어진 알파벳 이름을 만드는 최솟값을 구한다.
2-1. 최대 몇 개의 A가 연속으로 등장하느냐에 따라 최솟값을 구한다.
2-2. 가장 길게 연속된 A를 기준으로 짧은 쪽을 두 번 지나는 게 최솟값이다.
    즉, DBC'AA'FC 라는 문자열을 예로 들면 긴 쪽(왼쪽)을 두 번 지나 거꾸로 오른쪽으로 가는 것보다 거꾸로 먼저 가서 짧은 쪽(오른쪽)을 두 번 지난 뒤 처음으로 돌아와 왼쪽으로 가는 것이 좋다.
2-3. 연속된 A가 여러 개 있을 경우가 있으나 가장 길게 A가 연속된 부분이 기준이 된다.

3. 두 최솟값을 합한 답을 반환한다.
'''