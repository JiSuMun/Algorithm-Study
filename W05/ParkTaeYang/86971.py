def solution(n, wires):
    answer = 100
    if n ==2 :
        return 0
    for i in range(len(wires)):
        cut = wires[:i]+wires[i+1:]
        # print(cut)
        graph = [[]for _ in range(n+1)]
        visited = [False]*(n+1)
        for j in cut:
            a,b=j
            graph[a].append(b)
            graph[b].append(a)
        
        # print(graph)

        def line(start):
            cnt = 0
            stack = [start]
            visited[start] = True
            cnt += 1
            # print('입력')
            # print(cnt)

            while stack:
                cur = stack.pop()

                for adj in graph[cur]:
                    if not visited[adj]:
                        visited[adj] = True
                        cnt += 1
                        # print('스택입력')
                        # print(cnt)
                        stack.append(adj)
            return cnt

        cnt1 = 0
        cnt2 = 0
        cnt1 = line(1)
        # print('cnt1')
        # print(cnt1)
        for i in range(2,n):
            if visited[i]==False:
                cnt2 = line(i)
                break
        # print('cnt2')        
        # print(cnt2)
        answer = min(answer,abs(cnt1-cnt2))
        # print(answer)
    return answer


#복잡도는 for 문 순환 n , 자르기 n , while문 n O(N^3)
#n이 100이하라 실행시간이 길지 않음
n=2
w = [[1,2]]
print(solution(n,w))