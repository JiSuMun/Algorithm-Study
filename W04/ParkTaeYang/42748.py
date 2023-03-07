
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        x,y,z = commands[i]
        l = sorted(array[x-1:y])
        print(l)
        answer.append(l[z-1])
    return answer


# a = [1, 5, 2, 6, 3, 7, 4]
# c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# print(solution(a,c))
#시간복잡도는 commands 의 길이 N 에 정렬 NlogN O(N^2logN)