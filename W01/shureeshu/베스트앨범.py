# 베스트앨범
def solution(genres, plays):
    n = len(plays)
    play_list = [(genres[i], plays[i], i) for i in range(n)]
    plays_by_genres = {genre:sum(plays[i] for i in range(n) if genres[i] == genre) for genre in set(genres)}
    play_list.sort(key = lambda x: (-plays_by_genres[x[0]], -x[1], x[-1]))
    answer = [play_list[i][-1] for i in range(n) if i < 2 or (play_list[i][0] == play_list[i-1][0] == play_list[i-2][0]) == False]
    return answer