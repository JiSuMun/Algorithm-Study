# 올바른 괄호
# O(N)
def solution(s):
    answer = True
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True
    

    