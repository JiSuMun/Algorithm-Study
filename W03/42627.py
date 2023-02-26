import heapq
def solution(jobs):
    l = []
    heapq.heapify(jobs)
    t = 0
    heap = []
    while jobs or heap:
        while jobs:
            if jobs[0][0] <=t:
                x,y = heapq.heappop(jobs)
                heapq.heappush(heap,(y,x))
            else:
                break
        if not heap:
            t = jobs[0][0]
            continue

        b,a = heapq.heappop(heap)
        if t >= a:
            l.append(t+b-a)
            t += b
        else:
            l.append(t+b-a)
            t = b+a
    answer = sum(l)//len(l)
    return answer