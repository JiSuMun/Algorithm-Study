# 42579
# 시간 복잡도: for문 및 if문, in 사용 - O(N^2)
def solution(genres, plays):
    answer = []
    gen = []
    total = {}

    # 장르, 재생횟수, 고유번호를 담은 리스트
    gen = [[genres[i], plays[i], i] for i in range(len(genres))]
    gen = sorted(gen, key=lambda x: (x[0], -x[1], x[2]))    
    # 많이 재생될수록, 재생수가 같다면 고유번호가 낮을수록
    # -를 붙이면 현재와 반대차순으로 정렬


    for i in range(len(genres)):    # 장르별 total play 수를 저장하는 딕셔너리
        if genres[i] in total.keys():   # 만약 genres의 i번째가 total 딕셔너리 키값에 이미 있다면
            total[genres[i]] += plays[i]    # total의 키(genres[i])값의 value는 plays[i]를 더한 값이 된다.
        else:                               # 그게 아니라 genres의 i번째가 total 딕셔너리 키값에 없다면
            total[genres[i]] = plays[i] # total의 키(genres[i])값의 value는 plays[i]가 된다.

    total = sorted(total.items(), key=lambda x: -x[1])  # 재생수가 많은 순서대로 장르 정렬

    # 같은 장르 내에서는 최대 2곡까지 수록되도록 하는 코드
    for a in total: # 재생수가 많은 순서대로 장르를 정렬한 걸로 for문 돌리기
        count = 0
        for b in gen:   # 장르, 재생횟수, 고유번호를 담은 리스트로 for문 돌리기
            if a[0] == b[0]:    # 만약 total의 0번째(장르)와 gen의 0번째(장르)가 서로 일치한다면 
                count += 1      # count에 +1을 한다.
                if count > 2:   # 추가로 만약 count가 2를 초과한다면
                    break       # for문 탈출
                else:           # 그게 아니라 count가 2를 초과하지 않는다면 
                    answer.append(b[2]) # answer에 gen의 2번째(고유번호)를 추가한다.

    return answer


