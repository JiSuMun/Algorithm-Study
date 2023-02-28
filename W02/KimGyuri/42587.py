# Programmers 스택/큐 4. 프린터

# 시간복잡도: O(N^2)

from collections import deque

def solution(priorities, location):
    doc = deque(list(enumerate(priorities)))
    order = []

    while doc:
        if doc[0][1] < max(priorities):
            doc.append(doc.popleft())
        else:
            order.append(doc.popleft())
            priorities.remove(max(priorities))

    order = dict(order)
    answer = list(order.keys()).index(location) + 1
    
    return answer

'''
1. doc이라는 덱에 튜플 형태의 (문서번호(순서), 중요도) 값을 넣는다.
2. 가장 첫 번째 문서의 중요도를 확인하여 중요도가 더 높은 요소가 있으면 뒤로 보낸다.
3. 가장 중요한 문서일 경우 해당 요소를 덱에서 pop 하여 order라는 빈 리스트에 넣고 해당 중요도 값을 priorities에서 삭제한다.
4. 이 과정을 반복 완료한 뒤 order 리스트를 딕셔너리로 바꾼다.
5. 찾고자 했던 location 값이 몇 번째 있는지 확인하여 1을 더해 출력한다.  
'''
