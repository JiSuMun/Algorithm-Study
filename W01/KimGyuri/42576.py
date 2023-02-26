# Programmers 해시 2. 완주하지 못한 선수

# 시간복잡도
# sort: O(N log N)
# for 문: O(N)
# 리스트 요소 pop: O(1)
# 리스트 인덱스: O(1)

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for _ in range(len(completion)):
        p_name = participant.pop()
        c_name = completion.pop()
        if p_name == c_name:
            continue
        else:
            answer = p_name
            break
    else:
        answer = participant[0]
    
    return answer

'''
참가자와 완주자 리스트를 알파벳순으로 정렬한다.
참가자와 완주자 리스트에서 한 명씩 pop 하며 이름을 비교한다.
이름이 같을 경우 다음 이름을 pop 하며 계속 비교해나간다.
다를 경우 참가자 명단에 완주자 명단에 없는 이름이 들어 있다는 의미이므로 반복문을 멈추고 해당 이름을 출력한다.
중단 없이 반복이 끝난 경우 참가자 명단에 남아있는 이름을 출력한다.
'''
