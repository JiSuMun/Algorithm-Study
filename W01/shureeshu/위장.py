# 위장
def solution(clothes):
    answer = 1
    closet = dict()
    for item, category in clothes:
        closet[category] = closet.get(category, ["nude"])
        closet[category].append(item)
    for category in closet.keys():
        answer *= len(closet[category])
    return answer - 1