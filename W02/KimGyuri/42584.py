# Programmers 스택/큐 6. 주식가격

# 시간복잡도: O(N^2)

from collections import deque

def solution(prices):
    price_deque = deque(prices)
    answer = []
    
    while price_deque:
        p = price_deque.popleft()
        cnt = 0
        for price in price_deque:
            if price >= p:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
        
    return answer

'''
1. 주식 가격을 덱에 넣는다.
2. 제일 첫 번째 주식 가격부터 하나씩 pop 하여 'p'라는 변수에 넣고 나머지 주식 가격과 비교한다.
3. p와 나머지 주식 가격을 비교해가며 1씩 시간을 카운트하는데 비교한 가격이 더 높을 경우 멈춘다.
4. 카운트한 시간을 answer 리스트에 넣고 그 리스트를 출력한다.
'''
