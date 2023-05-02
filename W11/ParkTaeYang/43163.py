def solution(begin, target, words):
    answer = 0
    word_length = len(begin)
    visited = {begin:False}
    queue = [begin]
    for i in range(len(words)):
        visited[words[i]] = False
    
    if target not in words:
        return 0
    else:
        queue_size = len(queue)
        while queue_size > 0:
            if target in queue:
                return answer
            for q in range(queue_size):
                cur = queue.pop(0)
                if not visited[cur]:
                    visited[cur] = True
                    for j in range(len(words)):
                        check = True
                        for i in range(word_length):
                            if cur[i] != words[j][i]:
                                if not check:
                                    check = True
                                    break
                                else:
                                    check = False
                        if not check:
                            queue.append(words[j])
            
            queue_size = len(queue)
            answer += 1
            
        return answer