from collections import deque


def solution(prices): # O(N^2) worst case
    answer = [len(prices)-1]*len(prices)
    points = dict()
    for t, price in enumerate(prices):
        points.setdefault(price, deque([]))
        points[price].append(t)
        for past_price in list(points.keys()).copy():
            if price < past_price:
                for t1 in points[past_price]:
                    answer[t1] = t
                del points[past_price]
    for t1, t2 in enumerate(answer):
        answer[t1] = t2 - t1
    return answer


solution([1, 2, 3, 2, 3])
