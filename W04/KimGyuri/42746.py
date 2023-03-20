# Programmers 정렬 2. 가장 큰 수

# 시간복잡도: O(NlogN)

def solution(numbers):
    nums = list(map(str, numbers))
    nums.sort(key=lambda x: x * 3, reverse=True)
    answer = str(int(''.join(nums)))
    
    return answer

'''
1. numbers 배열에 담긴 수를 문자열로 바꾼다.
2. 자릿수를 세 자리로 맞추어 비교에 용이하게 하고 해당 기준에 따라 내림차순으로 정렬한다.
3. 정렬된 수를 하나의 문자열로 합친다.
4. 0이 연속된 문자열이 있을 수 있으므로 integer로 바꿨다가 다시 string으로 바꾸어 결괏값을 출력한다. 
'''
