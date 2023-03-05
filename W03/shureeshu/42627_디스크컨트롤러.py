# 디스크컨트롤러

"""

jobs : [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 
return : 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 

제한 사항
jobs의 길이는 1 이상 500 이하입니다.
jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

"""




def main():
    input_data = [[0, 3], [1, 9], [2, 6]]
    print(solution(input_data))

from heapq import heappush, heappop
def solution(jobs): # O(NlogN)
    # 작업이 시간 순으로 요청되도록 한다.
    jobs.sort(key = lambda x: x[0]) # O(NlogN)
    answer = 0
    # 현재 시점에 요청되어있는 작업 중 가장 짧은 것 부터 처리한다
    # 이를 위해 요청된 작업을 min_heap 으로 관리한다.
    priority_queue = []
    current_t = 0
    for job in jobs: # O(N)
        request_t = job[0]
        process_t = job[1]
        while request_t > current_t:
            if priority_queue:
                next_job = heappop(priority_queue) # O(log n)
                time_r = next_job[1]
                time_p = next_job[0]
                current_t += time_p
                answer += current_t - time_r
            else:
                # 요청을 기다린다
                current_t = request_t
        heappush(priority_queue, (process_t, request_t)) # O(log n)
        
    while priority_queue:
        next_job = heappop(priority_queue)
        time_r = next_job[1]
        time_p = next_job[0]
        current_t += time_p
        answer += current_t - time_r

    return answer//len(jobs)

main()

# 시간 복잡도 분석을 하면 다음과 같습니다.

# jobs.sort(key=lambda x: x[0]) : O(NlogN) - 주어진 작업 리스트를 요청 시간 순으로 정렬하는데 N개의 작업을 정렬하는데 O(NlogN) 시간이 소요됩니다.
# for loop : O(N) - 주어진 작업 리스트에 대해서 한 번씩 처리해야 하므로 N번 loop가 돌아갑니다.
# while loop : 최대 N번 loop가 돌아갈 수 있습니다. priority queue에서 pop을 하는데 걸리는 시간은 O(log n)이므로, while loop 전체의 시간 복잡도는 O(NlogN) 입니다.
# 따라서 이 코드의 전체 시간 복잡도는 O(NlogN)입니다.
