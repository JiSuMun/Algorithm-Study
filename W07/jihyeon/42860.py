# 42860 (조이스틱)
# 시간 복잡도: O(n^2)

def solution(name):
    answer = 0
    
    # 기본 최소 좌우이동 횟수는 name의 길이 - 1
    min_move = len(name) - 1
    
    for i, char in enumerate(name):

    	# 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
        
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer


# 풀이 방법이 떠오르질 않아 다른 분의 코드를 참고하여 풀이
# 사실 풀이 방법을 보고도 이해가 잘 가지 않는 문제였다..
