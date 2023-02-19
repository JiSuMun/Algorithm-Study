

def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(s) 
            #스택에 여는 괄호 넣고
        else:
            try:
                stack.pop()
            # 닫는 괄호 나오면 괄호가 만들어졌으니 pop 
            except:
                return False
            # 스택이 비어있는 경우  = ( 보다 ) 가 먼저 나와 괄호가 안 만들어지는 경우

    if stack:
        #만들어지지 않은 괄호가 있을 경우
        return False
    else:
        return True

    
#시간복잡도는 반복문 순회 O(N)




