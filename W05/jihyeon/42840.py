# 42840 (모의고사)
# 시간 복잡도: O(n)
def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    thr = [3,3,1,1,2,2,4,4,5,5]

    cnt = [0,0,0]
    right = []

    # answer의 각 요소를 순회하며 각 학생이 맞춘 문제 수를 계산
    for i in range(len(answers)):
        if answers[i] == one[(i%5)]:
            cnt[0] += 1
        if answers[i] == two[(i%8)]:
            cnt[1] += 1
        if answers[i] == thr[(i%10)]:
            cnt[2] += 1    

    # 각 학생이 맞춘 문제 수를 토대로 최고 점수를 받은 학생을 찾아 리스트에 추가하고 반환
    for j in range(3):
        if cnt[j] == max(cnt):
            right.append(j+1)
            
    return right

