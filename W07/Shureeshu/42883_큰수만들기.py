# 42883_큰수만들기

# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자
# number : 문자열 형식의 숫자
# k : 제거할 수의 개수
# return : 문자열 형식, number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자
def solution(number, k):
    answer = ''
    i = 0
    while len(number[i:]) > k:
        for digit in '9876543210':
            x = number.find(digit, i, i + k + 1)
            if x < 0: continue 
            else: break
        answer += number[x]
        i, k = x + 1, k - x + i
    
    return answer

# 1 : 앞에서 k + 1 개의 숫자 중 가장 큰 수 찾는다.
# 2 : 
number, k = "00",	1	#return    "775841"
print(solution(number, k))
number, k = "99",	1	#return    "775841"
print(solution(number, k))
number, k = "1924",	2, #return	"94"
print(solution(number, k))
number, k = "1231234",	3	#return    "3234"
print(solution(number, k))
number, k = "4177252841",	4	#return    "775841"
print(solution(number, k))

# str.find(sub[, start[, end]]) ## list에서 사용 불가
# Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.

# str.index(sub[, start[, end]]) ## list에서 사용 가능
# Like find(), but raise ValueError when the substring is not found.

# Note The find() method should be used only if you need to know the position of sub. To check if sub is a substring or not, use the in operator:
# >>> 'Py' in 'Python'