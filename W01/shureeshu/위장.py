# 위장
# 시간복잡도 : O(N)
def solution(clothes):
    answer = 1
    closet = dict()
    for item, category in clothes: # N
        closet[category] = closet.get(category, ["nude"])
        closet[category].append(item)
    for category in closet.keys(): # max 30
        answer *= len(closet[category]) # 1
    return answer - 1

"""

의상의 종류를 key, 해당 종류 의상의 이름들의 리스트를 value로 하여 dictionary를 만든다.
모든 의상 종류에 대해 default value로 "nude"를 추가한다.
dictionary 의 key를 루핑하며 value에 들어있는 원소의 수를 product 한다.
아무것도 입지 않은 경우를 제외한다.

"""

# 제한사항
# clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
# 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
# 같은 이름을 가진 의상은 존재하지 않습니다.
# clothes의 모든 원소는 문자열로 이루어져 있습니다.
# 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
# 스파이는 하루에 최소 한 개의 의상은 입습니다.