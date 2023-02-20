# 42578 -- 평소 풀이 방식
clothes = []
clothlist = []

for i in range(3):
    cloth = list(input().split())
    clothes.append(cloth)

for a in range(len(clothes)):
    clothlist.append(clothes[a][0])   

for b in range(len(clothes)-1):
    for c in range(len(clothes)-1):
        if clothes[b][1] != clothes[c+1][1]:
            clothlist.append((clothes[b][0], clothes[c+1][0]))
print(len(clothlist))


def solution(clothes): # 위 코드를 프로그래머스에 적용 시킨 것. 몇 개만 맞고 틀림ㅠ
    clothlist = []
    
    for a in range(len(clothes)):
        clothlist.append(clothes[a][0])   
        
    for b in range(len(clothes)-1):
        for c in range(len(clothes)-1):
            if clothes[b][1] != clothes[c+1][1]:
                clothlist.append((clothes[b][0], clothes[c+1][0]))
    answer = len(clothlist)
    
    return answer


# 정답 - 딕셔너리를 사용해야 함
# 시간 복잡도: for문 순회 및 in 사용 - O(N^2)
def solution(clothes):
    cloth = {}  # cloth 딕셔너리 생성
    answer = 1
    
    for a in clothes:   # 입력 값이 있는 리스트에서 for문 생성
        if a[1] in cloth.keys():    # 만약 a번째 옷의 '종류'가 cloth 딕셔너리 키 값에 이미 있다면
            cloth[a[1]].append(a[0])    # a번째 옷을 그 키 값의 value로 추가해준다.
        else:                       # 그게 아니라 a번째 옷의 '종류'가 cloth 딕셔너리 키 값에 없다면
            cloth[a[1]] = [a[0]]    # a번째 옷의 '종류'를 키 값으로, 옷을 value로 생성해준다.
    
    for value in cloth.values():    # cloth 딕셔너리 value로 for문 생성
        answer *= len(value) + 1    # answer는 answer * (value의 길이 + 1)이 된다.
                                    # 여기서 +1을 하지 않을 경우, 만약 첫번째 len(value)값이 2, 두번째 len(value) 값이 1이라 가정하면,
                                    # 첫번째 answer는 2가 되고, 두번째 answer는 len(value)가 1이기에 똑같이 2가 된다.
                                    # 이럴 경우 옷의 조합을 출력을 출력해야 하는 문제의 답과 일치하지 않기 때문에 +1을 해줘야한다.
    
    return answer - 1   # 이렇게 되면 아무것도 입지 않은 경우, 하나만 입은 경우, 종류별로 입는 경우가 되고,
                        # 아무것도 입지 않는 경우는 빼줘야 하기 때문에 -1을 하여 answer를 리턴해준다.

# answer = answer * len(value) + 1 과
# answer *= len(value) + 1 의 차이를 알게됨
# 밑에 껀 answer = answer * (len(value) + 1)로 처리한다는 것을 알게 되었다.

