# 42587 (프린터)
# 시간 복잡도: while문 안에 for문 - O(n log n)
def solution(priorities, location):
    answer = 0

    while True:
        max_n = max(priorities) # priorities의 max값을 max_n에 넣어줌
        for i in range(len(priorities)):    # priorities 리스트를 처음부터 확인
            if max_n == priorities[i]:      # 만약 리스트의 max값과 리스트의 요소가 일치하면
                answer += 1                 # 프린트한 것으로 간주하고 answer += 1
                priorities[i] = 0           # 프린트한 요소는 0으로 초기화
                max_n = max(priorities)     # priorities의 max값을 다시 구해줌
                if i == location:           # 추가로 i와 location이 일치하면
                    return answer           # answer를 반환한다.
 