# 42577
def solution(phone_book):
    phone_book.sort()
    b = []
    
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            b.append('false')
            break
        else:
            b.append('true')
            
    if 'false' in b:
        answer = False
    else:
        answer = True
    return answer
# 위 코드는 2, 32가 있으면 32에 결국 2가 있어 false로 판정되기 때문에 오답



# 정답
# 시간 복잡도: for문 순회 및 if문 - O(N)
def solution(phone_book):
    phone_book.sort() # phone_book 리스트 정렬
    b = []        # 리스트 b 생성

    for i in range(len(phone_book)-1):    # phone_book 리스트의 길이 -1만큼의 for문 범위 생성
        if phone_book[i+1].startswith(phone_book[i]): # 만약 phone_book[i+1]이 phone_book[i]로 시작한다면
            b.append('false')     # 리스트b에 false를 추가한다.
            break                 # 그러면 더 이상 phone_book 리스트를 확인할 필요가 없으므로 for문 break
        else:                     # 그게 아니라면
            b.append('true')      # 리스트b에 true 추가

    if 'false' in b:      # 만약 리스트b에 false가 있다면
        answer = False    # answer에 False 반환
    else:                 # 만약 리스트b에 false가 없다면
        answer = True     # answer에 True 반환
    return answer

# 수업 때 잠깐 들었던 startswith을 다시 한번 찾아보고 언제 쓰이는지 알게 됨
