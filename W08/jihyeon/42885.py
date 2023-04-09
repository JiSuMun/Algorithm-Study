# 42885 (구명보트)
# 시간 복잡도: O(n log n)

def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1     # indexing으로 비교하기 위해 배열의 길이에서 1을 빼줌
    while a <= b:
        answer += 1
        if people[b] + people[a] <= limit:  # 가장 몸무게가 큰 사람과 작은 사람을 더해 limit 값보다 작거나 같으면 태우고, 크면 가장 큰 사람만 태움
            a += 1
        b -= 1
    return answer


