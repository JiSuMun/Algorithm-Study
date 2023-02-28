# Programmers 스택/큐 1. 같은 숫자는 싫어

# 시간복잡도: O(N)

from collections import deque

def solution(arr):
    arr = deque(arr)
    answer = []
    answer.append(arr.popleft())
    
    while arr:
        if arr[0] == answer[-1]:
            arr.popleft()
        else:
            answer.append(arr.popleft())
    return answer

'''
1. arr 배열을 덱 객체로 만든다.
2. 먼저 arr의 첫 번째 수를 pop 하여 'answer'라는 빈 리스트에 넣는다.
3. 리스트에 담긴 숫자 중 제일 마지막 수와 덱의 첫 번째 수를 비교하여 같으면 해당 수를 pop 하여 삭제하고 다를 경우 해당 수를 pop 하여 'answer'에 추가한다.
4. 이 과정을 덱이 빌 때까지 반복한다.
5. 연속된 수를 제거한 배열이 담긴 answer 리스트를 출력한다.
'''
