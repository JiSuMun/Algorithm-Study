# Programmers 스택/큐 3. 올바른 괄호

# 시간복잡도: O(N)

def solution(s):
    lst = []
    for i in range(len(s)):
        if s[i] == '(':
            lst.append(s[i])
        else:
            try:
                lst.pop()
            except:
                return False
    else:
        if lst:
            return False
        else:
            return True

'''
1. 문자열 속 괄호를 하나씩 불러오며 확인한다.
2. 여는 괄호일 경우 빈 리스트에 추가한다.
3. 닫는 괄호일 경우 빈 리스트에 담긴 여는 괄호를 하나씩 pop 하며 짝을 맞춰 삭제한다.
4. 아무것도 없는 리스트에서 pop을 하는 경우 닫는 괄호가 먼저 나온 유효하지 않은 문자열이기 때문에 False를 출력하고 반복문을 멈춘다.
5. 반복문이 모두 돌아간 후 리스트에 값이 남아있는 경우 짝이 맞지 않은 괄호가 남아있다는 의미이므로 false를 출력하고, 리스트가 비어있는 경우 true를 출력한다.
'''
