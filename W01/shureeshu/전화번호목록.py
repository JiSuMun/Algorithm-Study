# 전화번호 목록
def solution(phone_book):
    phone_book.sort()
    b = phone_book.pop()
    while phone_book:
        a = phone_book.pop()
        if b[:len(a)] == a:
            return False
        else:
            b = a
    return True

