# 12909 (올바른 괄호)
# 시간 복잡도: for문 - O(N)
def solution(s):
    answer = True
    m = 0
    
    for i in range(len(s)): # 입력값의 전체 길이로 for문 돌림
        if s[0] == ')' or s[-1] == '(': # 만약 리스트s의 첫번째가 ')'고, 마지막이 '('면  
            answer = False              # 괄호가 닫혔다는 뜻이 아니므로 answer = false
            break                       # for문 탈출

        if s[i] == '(':                 # 리스트s의 첫번째가 '('고, 마지막이 ')'인데 i번째 괄호가 '('라면 
            m += 1                      # m += 1
        else:                           # 그게 아니라 i번째 괄호가 ')'라면
            m -= 1                      # m -= 1
            if m < 0:                   # 추가로 현재 m의 값이 0보다 작다면 (괄호의 합이 0이지만 '())(()' 같이 합이 맞지 않는 괄호가 발생할 시를 대비한 코드 / '())'와 같은 괄호가 있으면(이때 m의 값이 0보다 작음))
                answer = False          # answer = false
                break                   # for문 탈출

    if s[0] == '(' and s[-1] == ')':    # 만약 리스트s의 첫번째가 '('고, 마지막이 ')'인데
        if m == 0:                      # 추가로 m의 값이 0이면
            answer = True               # answer = True 
        else:                           # m의 값이 0이 아니라면
            answer = False              # answer = False
    
    return answer   # answer값 반환
