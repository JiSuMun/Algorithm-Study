
# genres = ["classic","classic","classic","classic","classic"]
# plays = [500,600,500,600,700]

# def solution(genres, plays):
#     d = {}
#     answer = []
#     igp = [] #(index,(genres,plays))를 조합하여 리스트생성
#     for i in range(len(genres)):
#         d[genres[i]] = d.get(genres[i],0)+plays[i]
#         igp.append((i,(genres[i],plays[i])))
#     l2 = sorted(d.items(),key = lambda x : -x[1])
#     # 딕셔너리 생성후 value에 대해 내림차순으로 정렬

#     igp = sorted(igp,key = lambda x: x[1],reverse=True)
#     # 리스트 생성후 tuple에 대해 내림차순으로 정렬
#     for i in l2:
#         cnt = 0
#         for j in igp:
#             if i[0]== j[1][0]:
#                 answer.append(j[0])
#                 cnt +=1
#             if cnt==2:
#                 break
#             #장르당 2개까지 리스트에 추가
#     return answer


# 시간복잡도는 sorted를 사용했기에 O(nlogn)
# 장르의 갯수 제한이 없다면 O(n^2) 

genres = ["pop", "classic", "pop", "pop","jazz", "pop", "suck"]
plays = [800, 600, 800, 800, 8000, 2500, 1]
gen = list(enumerate(zip(genres,plays)))
print(gen)