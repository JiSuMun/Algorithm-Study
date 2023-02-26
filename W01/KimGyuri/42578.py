# Programmers 해시 4. 위장

# 시간복잡도
# for 문: O(N)
# 딕셔너리 데이터 저장: O(1)
# 리스트 인덱스: O(1)
# 리스트 길이: O(1)

def solution(clothes):
    answer = 1
    dict = {}
    for cloth in clothes:
        if cloth[1] not in dict:
            dict[cloth[1]] = [cloth[0]]
        else:
            dict[cloth[1]] += [cloth[0]]
    
    for key in dict.keys():
        answer *= len(dict[key]) + 1
    return answer - 1

'''
딕셔너리에 의상의 종류(key)/의상의 이름(value)을 저장한다.
종류별 의상 개수에 1(해당 종류의 의상을 입지 않는 경우)을 더해 곱해 의상을 조합할 수 있는 모든 경우의 수를 구한다.
스파이는 최소한 한 개의 의상은 입기 때문에 어떠한 의상도 입지 않는 경우 1을 빼고 답을 출력한다.
'''
