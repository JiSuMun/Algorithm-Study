def solution(number, k):
    answer = []

    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)

    return ''.join(answer[:len(answer) - k])

# 시간복잡도는 for 문 순환 O(N)