a = [9,969,98,10,100,1,12]

# def solution(numbers):
#     answer = ''
#     ans = list(map(str, numbers))
#     ans = sorted(ans, reverse = True) 
#     print(ans)
#     answer = str(int("".join(ans)))
#     return answer

# print(solution(a))


def solution(numbers):
    answer = ''
    ans = list(map(str, numbers))
    ans = sorted(ans, key = lambda x: x*3, reverse = True) 
    answer = str(int("".join(ans)))
    return answer

print(solution(a))

# 시간복잡도는 리스트 정렬 O(NlogN)