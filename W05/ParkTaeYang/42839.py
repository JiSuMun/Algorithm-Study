from itertools import permutations
def isprime(n):
    if n==0 or n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True

def solution(numbers):
    lst = list(numbers)
    p = []
    p = set(p)
    for q in range(1,len(lst)+1):
        for i in permutations(lst,q):
            j = ''.join(i)
            p.add(int(j))
    answer = 0
    for i in p:
        if isprime(i)==True:
            answer +=1
    return answer




#시간복잡도는 numbers 로만들어지는 순열의 개수 N 에 소수확인 N O(N^2) 

n = input()
print(solution(n))