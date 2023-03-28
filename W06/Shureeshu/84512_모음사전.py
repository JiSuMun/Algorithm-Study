# 84512_모음사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

# 제한사항
# word의 길이는 1 이상 5 이하입니다.
# word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.

def solution(word):
    answer = 0
    order = {
        'A' : 0,
        'E' : 1,
        'I' : 2,
        'O' : 3,
        'U' : 4,
    }
    word = ''.join([word, ' '*(5-len(word))])
    for i, char in enumerate(word):
        if char == ' ':
            break
        else:
            answer += sum(5**i for i in range(5-i))*order[char] + 1
    return answer


# 'AEIOU' 의 순서 : 'AEI'의 순서 + 2글자 사전에서 'OU'의 순서
# 'A'의 순서 + 4글자 사전에서 'EIOU'의 순서
# 'A'의 순서 + 4글자 사전에서 'E'의 순서 + 3글자 사전에서 'IOU'의 순서
# 'AEI'의 순서 : 'AE'의 순서 + 3글자 사전에서 'I'의 순서