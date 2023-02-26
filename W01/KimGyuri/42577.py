# Programmers 해시 3. 전화번호 목록

# 시간복잡도
# sort: O(N log N)
# for 문: O(N)
# 리스트 인덱스: O(1)
# 리스트 길이: O(1)

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    else:
        return True

'''
전화번호 배열을 오름차순으로 정렬한다.
정렬 후에는 n번째 요소와 n+1번째 요소만 확인하면 되므로 n+1번째 번호에서 n번째 요소의 길이만큼만 앞 숫자를 비교한다.
두 수가 같을 경우 false를 출력한다.
두 수가 다를 경우 n+1번째 요소와 n+2번째 요소를 비교한다.
위 과정을 반복했을 때 같은 수가 없으면 true를 출력한다.
'''
