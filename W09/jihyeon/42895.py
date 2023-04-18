# 42895 (N으로 표현)
# 시간 복잡도: 전체 코드의 시간 복잡도는 첫번째 루프에서 O(1)이고, 두번째 루프에서 O(1) + O(2) + ... + O(i^2) = O(i^3)이므로, 최악의 경우에는 O(8^3) = O(512)입니다. 즉, 입력 크기에 상관없이 실행 시간이 일정합니다.

def solution(N, number):
    answer = -1
    dp = []
    
    for i in range (1,9) :  # i = N의 개수
        all_case = set()
        check_num = int(str(N)* i)   # {N}, {NN} , {NNN}...
        all_case.add(check_num)
        
        for j in range(0, i-1): # j개를 사용해서 만든 값들
            for op1 in dp[j]:
                for op2 in dp[-j-1] :
                    all_case.add(op1 - op2)
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(op1 // op2)
                        
        if number in all_case:
            answer = i
            break
            
        dp.append(all_case) 
        
    return answer


# 만약 N이 5일 경우
# N이 i 개 만큼 있는 set을 생성
# dp[1] 일 경우, {5} / dp[2] 일 경우 {5+5, 5-5, 5//5, 5*5}이기 때문에 이전(dp[1])의 구성요소의 사칙 연산 결과로 구성 돼있음
# dp[3]의 경우 555 , (dp[1] 연산 dp[2]) , (dp[2] 연산 dp[1])이 되는것을 확인할 수 있음
# 만들어진 dp[i] set 에서 number가 존재하면 i 반환
# 끝까지 발견 못하면 -1 출력
