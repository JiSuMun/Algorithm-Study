# Programmers 탐욕법(Greedy) 3. 큰 수 만들기

def solution(number, k):
    answer = []
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])

'''
1. 숫자를 맨 앞의 수부터 하나씩 스택에 넣는다.
2. 앞서 넣은 수보다 뒤의 수가 더 크고 k가 0보다 커서 제거할 수 있다면 앞선 수를 빼고 뒤의 수를 넣는다.
3. 이 과정을 반복한다.
4. 스택의 가장 마지막 수와 같거나 작고 k가 0일 경우에는 스택에서 수를 빼는 것이 불가능하므로 앞에서부터 원하는 자릿수까지만 잘라 출력한다.
'''