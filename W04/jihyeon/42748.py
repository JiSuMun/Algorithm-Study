# 42748 (K번째수)
# 시간 복잡도: O(kn log n) - 여기서 k는 commands의 길이, n은 array의 길이
def solution(array, commands):
    answer = []

    for i in commands:
        arr = array[i[0]-1:i[1]]    # arr은 array에서 commands 범위 만큼을 담은 리스트 
        arr = sorted(arr)           # arr 정렬  
        answer.append(arr[i[2]-1])  # arr리스트에서 원하는 값을 answer 리스트에 추가 

    return answer   # answer 반환

