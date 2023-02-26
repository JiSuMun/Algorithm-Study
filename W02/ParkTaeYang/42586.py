def solution(progresses, speeds):
    answer = []
    while progresses:
        num = len(progresses)
        for i in range(num):
            progresses[i] += speeds[i]
        
        cnt = 0
        for i in range(num):
            if progresses[i]>=100:
                cnt+=1
            else:
                break
        for i in range(cnt):
            progresses.pop(0)
            speeds.pop(0)

        if cnt != 0 :
            answer.append(cnt)
        

    return answer


# 통과
# 앞선 문제(12906)의 시간초과로 deque 와 deepcopy 사용을 하지 않고 먼저 풀어보려고 pop(0)를 사용했으나, 
# 문제 실행결과에서 시간측정 과정은 하지않고 정확성 측정만으로 통과

# 복잡도는 while문 안에 cnt만큼 pop(0)여서 N^3 보다는 작은데
# while문이 커지면 cnt가 작아지고 while문이 작아지면 cnt가 커져서 어떻게 계산해야하는지 잘모르겠음