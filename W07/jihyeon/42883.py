# 42883 (큰 수 만들기)
# 시간 복잡도

def solution(number, k):
    num = []

    # 큰 수는 일단 앞 자릿수가 커야함.
    # number에서 앞에 있는 숫자부터 num 리스트에 넣어주고 push되는 값보다 작은 값이 있으면 pop하고, pop 횟수는 삭제된 k만큼 수행되는 것이다.
    for i in number:
        while num and num[-1] < i and k > 0:
            num.pop()
            k -= 1
        num.append(i)

    # 아직 제거되지 못한 숫자를 뒤에서 삭제
    if k > 0:
        num = num[:-k]

    return ''.join(num)
