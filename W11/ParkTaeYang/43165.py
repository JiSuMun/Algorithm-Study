
def solution(numbers, target):
    cnt = 0
    stack = [(0,0)]
    while stack:
        s,l = stack.pop()
        if l>len(numbers):
            continue
        if l==len(numbers) and target == s:
            cnt +=1
        stack.append((s+numbers[l-1],l+1))
        stack.append((s-numbers[l-1],l+1))
        
    return cnt

# 시간복잡도는 더하기 뺴기 두가지 경우의 수가 n개 O(2^n)