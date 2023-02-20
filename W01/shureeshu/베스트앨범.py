# 베스트앨범
# 시간복잡도 : O(NlogN)
def solution(genres, plays):
    n = len(plays) # 1
    play_list = [(genres[i], plays[i], i) for i in range(n)] # N
    plays_by_genres = {genre:sum(plays[i] for i in range(n) if genres[i] == genre) for genre in set(genres)} # 100N
    play_list.sort(key = lambda x: (-plays_by_genres[x[0]], -x[1], x[-1])) # NlogN
    answer = [play_list[i][-1] for i in range(n) if i < 2 or (play_list[i][0] == play_list[i-1][0] == play_list[i-2][0]) == False] # N
    return answer

"""

1 play_list : (장르, 재생횟수, 곡 번호)의 튜플이 담긴 리스트를 만든다.
2 plays_by genres : play_list를 활용하여 장르를 key로 하고 각 장르에 해당하는 곡들의 재생 횟수의 합을 value로 하는 dictionary를 만든다.
3 play_list.sort() : plays_by_genres 를 활용하여 play_list를 조건에 맞게 sorting한다.
4. 정렬된 play_list에서 각 장르 별로 2개 이하의 곡만 추출한다.

"""

# 제한사항
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.