# 기능개발
# O(N)
from math import ceil
def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    working_day = 0
    publishing = 0
    while progresses:
        current_progress = progresses.pop()
        progress_per_day = speeds.pop()
        if current_progress + progress_per_day * working_day >= 100:
            publishing += 1
        else:
            if publishing > 0:
                answer.append(publishing)
                publishing = 0
            working_day = ceil((100 - current_progress)/progress_per_day)
            publishing += 1
    answer.append(publishing)
    return answer