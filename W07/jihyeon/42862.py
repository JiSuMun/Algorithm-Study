# 42862 (체육복)
# 시간 복잡도: O(n log n)

def solution(n, lost, reserve): 
    answer = 0 
    
    # 여벌의 체육복을 가져온 학생이 체육복을 도난당한 학생일 수 있으므로 각 배열에서 set을 하고 빼준다. 
    reserve_set = set(reserve)-set(lost) 
    lost_set = set(lost)-set(reserve) 
    
    # 여벌의 체육복을 가져온 학생은 자신의 바로 앞,뒷번호의 학생에게만 체육복을 빌려줄 수 있기 때문에 만약 자신의 바로 앞,뒷번호 학생이 lost 배열에 있다면 체육복을 빌려준 걸로 가정하고 lost 배열에서 지워준다.
    for i in reserve_set: 
        if i-1 in lost_set: 
            lost_set.remove(i-1) 
            
        elif i+1 in lost_set: 
            lost_set.remove(i+1) 
            
    # 전체 학생 수에서 체육복을 도난당한 학생 수를 빼준다.
    answer = n - len(lost_set)
    
    return answer
