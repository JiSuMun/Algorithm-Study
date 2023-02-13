# def solution(participant, completion):
#     for i in completion:
#         participant.remove(i)
#     answer = participant[0]
#     return answer


# 시간초과 포문안의 remove로 시간복잡도 O(n^2)

def solution(participant, completion):
    participant = sorted(participant) 
    completion = sorted(completion)   
    # 문자열을 정렬
    print(participant,completion)
    for i in range(len(completion)):  
        # 길이가 짧은 비교군으로 반복문 순환
        a = participant.pop()
        b = completion.pop()
        # 맨 끝을 pop하면서 비교
        if a!=b:
            answer = a                
            # pop한 값이 다를 경우 b에 없는 원소이므로 a에서 pop한 값을 return
            break
    else:
        answer = participant[0]       
        # for문이 len(completion) 까지 반복된다면 particpant의 맨 앞 원소가 completion에 없는 원소
    return answer


# 통과

# 시간복잡도는 sorted를 사용했기에 O(nlogn)