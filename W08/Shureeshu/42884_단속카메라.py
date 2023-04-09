def solution(routes):
    answer = 1
    
    # 정렬
    routes.sort()
    start, end = -30000, 30000
    
    # 현재 구간이 다음 구간과 겹치지 않을때에만 새 카메라를 추가한다.
    for entry_point, exit_point in routes:
        if end < entry_point:
            answer += 1
            start, end = entry_point, exit_point
        else:
            start = max(start, entry_point)
            end = min(end, exit_point)
            
    return answer


# 시간복잡도 O(nlogn)