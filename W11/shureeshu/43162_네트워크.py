def solution(n, computers):

    answer = 0
    visited = [False]*n

    for computer in range(n):

        # 방문하지 않은 Node에 대하여
        if not visited[computer]:
            answer += 1

            # DFS (연결된 모든 Node를 방문처리)
            stack = [computer]
            while stack:
                i = stack.pop()
                for j, is_linked in enumerate(computers[i]):
                    if is_linked and not visited[j]:
                        stack.append(j)
                visited[i] = True


    return answer

# return 네트워크의 갯수