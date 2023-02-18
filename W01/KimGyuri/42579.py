# Programmers 해시 5. 베스트 앨범

# 시간복잡도
# for 문: O(N)
# 딕셔너리 데이터 저장: O(1)
# 리스트 인덱스: O(1)
# 리스트 길이: O(1)

def solution(genres, plays):
    answer = []
    dict = {}
    count_dict = {}

    for i in range(len(genres)):
        if genres[i] not in dict:
            dict[genres[i]] = [(plays[i], i)]
            count_dict[genres[i]] = plays[i]
        else:
            dict[genres[i]] += [(plays[i], i)]
            count_dict[genres[i]] += plays[i]

    for k, v in sorted(count_dict.items(), key = lambda x: x[1], reverse = True):
        if len(dict[k]) >= 2:
            for j in range(2):
                answer.append(sorted(dict[k], key = lambda x: x[0], reverse = True)[j][1])
        else:
            answer.append(dict[k][0][1])
    
    return answer

'''
딕셔너리에 노래의 장르(key)/튜플 (재생 횟수, 고유번호)(value)를 저장한다.
그리고 또 다른 딕셔너리에 노래의 장르(key)/재생 횟수 합(value)을 저장한다.
재생 횟수 합이 높은 장르부터 불러와 재생 횟수 기준으로 내림차순으로 정렬하고 2개 노래의 고유번호를 출력한다.
장르에 속한 곡이 하나라면 하나의 곡만 선택한다.
'''
