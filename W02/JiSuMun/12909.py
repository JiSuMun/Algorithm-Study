# 올바른 괄호
# 스택/큐
# 시간복잡도: for문 => O(N)
def solution(s):
    ans = True
    res = []
    for i in s:
        if i == '(': res.append(i)
        else:
            if not res:
                ans = False
            else:
                res.pop()
    if res: ans = False
    return ans

"""
미리 ans에 True를 줘서 False의 조건 외에는 True 반환하도록 함
"""