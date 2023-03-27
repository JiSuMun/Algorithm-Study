lst1=[1,2,3,4,5]*2000
lst2=[2,1,2,3,2,4,2,5]*1250
lst3=[3,3,1,1,2,2,4,4,5,5]*1000

def solution(answers):
    cnt1 = 0; cnt2=0; cnt3=0
    for i in range(len(answers)):
        if answers[i]==lst1[i]:
            cnt1+=1
        if answers[i]==lst2[i]:
            cnt2+=1
        if answers[i]==lst3[i]:
            cnt3+=1

    answer = []
    m = max(cnt1,cnt2,cnt3)
    if m == cnt1:
        answer.append(1)
    if m == cnt2:
        answer.append(2)
    if m == cnt3:
        answer.append(3)    
    
    return answer

# 시간복잡도는 answers의 길이 순회 O(N)