




# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: (f(x), len(x)),  reverse = True) # O(NlogN)
    answer = ''.join(numbers)
    if int(answer):
        return answer
    else:
        return '0' # 입력이 모두 0인 경우....!!!!!!!

def f(x):
    if len(x) < 4:
        return (4*x)[:4]
    else:
        return x

