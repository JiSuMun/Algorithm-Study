# 42746 (가장 큰 수)
# 시간 복잡도: O(n log n) - sort 함수의 시간 복잡도는 O(n log n)
def solution(numbers):
    numbers = list(map(str, numbers))           # numbers 리스트 속성을 문자열로 바꿈
    numbers.sort(key=lambda x:x*3, reverse=True) # key=lambda x:x*3을 사용하는 이유는 문제 조건에서 입력되는 숫자의 최대 크기가 0 이상 1,000 이하라고 제시했기 때문이다. key 함수를 사용해 가장 큰 수를 만들기 위해서 각 숫자를 세 자리수로 만들어주는 작업이 이루어진다.
    return str(int(''.join(numbers)))           # 조합된 문자열을 다시 숫자로 변환하며 출력

