# 전화번호 목록
# 시간 복잡도: NlogN + N -> NlogN
def solution(phone_book):
    phone_book.sort() # NlogN
    b = phone_book.pop()
    while phone_book: # N
        a = phone_book.pop() # 1
        if b[:len(a)] == a: # len(a) <= 20
            return False
        else:
            b = a
    return True

"""

1 : 사전 순으로 정렬된 문자열은 반드시 접두어가 그 접두어가 붙어있는 단어보다 앞에 등장한다.
2 : 사전 순으로 정렬된 문자열에서 어떤 접두어가 어떤 단어에 붙어있다면 그 접두사와 그 단어 사이에 있는 모든 단어에는 그 접두사가 붙어있다.
3 : 접두어가 하나라도 존재할 경우 False를 반환한다

전화번호 문자열들을 사전 순으로 정렬한 후, 마지막 문자열부터 모든 문자열에 대해 바로 앞에 위치한 문자열이 접두어인지 확인한다. 반복문 진행 중 접두어를 발견하면 False를 반환하고 모든 문자열이 접두어가 아니라면 True를 반환한다 

"""
# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.