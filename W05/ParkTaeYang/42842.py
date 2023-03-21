def solution(brown, yellow):
    for i in range(1,brown//2+1):
        for j in range(1,brown//2+1):
            if 2*i+2*j-4 == brown and (i-2)*(j-2) == yellow:
                answer = [max(i,j),min(i,j)]
                return answer
    
a,b=map(int,input().split())
print(solution(a,b))
#시간복잡도는 brown//2의 제곱 순회 O(N^2)