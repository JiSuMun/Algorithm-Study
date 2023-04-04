def solution1(name):
    answer = 0
    for i in name:
        answer += min((ord(i)-ord('A'),ord('Z')-ord(i)+1))
        
    print(answer)
    lst = list(name)
    lst[0] = 'A'
    i = 0
    l = len(lst)
    while True:
        move_right = 1
        move_left = -1
        while lst[(i+move_right)%l] == 'A':
            move_right +=1
            if move_right>l:
                break
        if move_right>l:
                break
        while lst[i+move_left] == 'A':
            move_left -=1

        if move_right<-move_left:
            answer +=move_right
            i += move_right
            lst[i] = 'A'
        else:
            answer += -move_left
            i += move_left
            lst[i] = 'A'
        print(*lst)
        print(answer)
    return answer

n = 'BBBBAAAABA'
print(solution1(n))
#시작위치가 첫번째 오답

def solution2(name):
    answer = 0
    name = list(name)
    min_move = len(name) - 1
    for i in range(len(name)):
        answer += min(ord(name[i]) - ord('A') , ord('Z') - ord(name[i]) + 1)
        next_d = i + 1
        up_d = 0
        while next_d < len(name) and name[next_d] == 'A':
            next_d += 1
        min_move = min(min_move, i + i + len(name) - next_d)
        min_move = min(min_move, (len(name)-next_d) * 2 + i)
        print(*name)
    answer += min_move
        
    return answer

n = 'BBBBAAAABA'
print(solution2(n))

# 시간복잡도는 O(N^2)