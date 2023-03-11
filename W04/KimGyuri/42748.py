# Programmers 정렬 1. K번째 수

# 시간복잡도: O(N*MlogM)
# N은 commands 리스트의 길이이며, M은 각 명령어에서 슬라이싱한 리스트의 길이

def solution(array, commands):
    answer = []
    
    for n in range(len(commands)):
        i, j, k = commands[n]
        lst = array[i-1:j]
        lst.sort()
        answer.append(lst[k-1])
    
    return answer

'''
1. commands 리스트의 길이만큼 반복문을 돌린다.
2. 하나의 command 속 요소를 각각 i, j, k로 받는다.
3. 배열 array의 인덱스가 i-1번인 숫자부터 j-1번인 숫자까지 자르고 정렬한다.
4. 3에서 정렬된 배열에서 인덱스 k-1번 숫자를 answer 리스트에 추가한다.
5. 반복문이 종료되면 answer 리스트를 출력한다.
'''
