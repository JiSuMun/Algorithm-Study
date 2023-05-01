def solution(n, computers):
    answer = 0
    visited = [False]*n
    for computer in range(n):
        if not visited[computer]:
            answer += 1
            stack = [computer]
            while stack:
                i = stack.pop()
                for j, is_linked in enumerate(computers[i]):
                    if is_linked and not visited[j]:
                        stack.append(j)
                visited[i] = True
    return answer

# return 네트워크의 갯수