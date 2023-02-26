# 프린터

# O(N^2)
def solution(priorities, location):
    answer = 0
    while priorities:
        answer += 1
        next_printed = priorities.index(max(priorities))
        if next_printed == location:
            return answer
        else:
            if next_printed < location:
                location -= next_printed+1
            else:
                location += len(priorities) - next_printed - 1                        
            priorities = (priorities + priorities[ :next_printed])[next_printed + 1 :]
    return answer