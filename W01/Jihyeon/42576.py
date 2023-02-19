# 42576
# 시간 복잡도: for문 순회 및 != 사용 - O(N)
def solution(participant, completion):
    participant.sort() # 참여선수 정렬
    completion.sort() # 완주자 정렬
    
    for i in range(len(completion)): # 완주자 길이의 for문을 돌리고
        if participant[i] != completion[i]: # 만약 참여선수 i번째가 완주자 i번째와 같지 않다면
            return participant[i]   # 참여선수 i번째 반환
        
    return participant[-1] # for문을 돌리고도 아직 찾지 못했다면 남은 선수가 리스트 마지막에 위치한다는 말이기에
                            # for문 밖에서 참여선수 리스트의 마지막을 반환해준다.


# 간단하면서도 생각을 좀 해야하는 것 같은 문제..!
# return의 정의에 대해 찾아보게 된 계기가 됨
# 간단하지만 효율성을 테스트하는 문제도 있다는 것을 알게됨
