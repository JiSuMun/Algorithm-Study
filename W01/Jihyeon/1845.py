# 1845 -- 평소 풀이 하던 방식
nums = list(map(int, input().split()))
num = []

for i in range(len(nums)):
    if nums[i] not in num:
        if len(num) == len(nums)//2:
            break
        else:
            num.append(nums[i])
    else:
        pass
print(len(num))

# --- 정답
# 시간 복잡도: if문 사용 - O(N)
def solution(nums):
    answer = 0
    nums_set = set(nums) # set으로 폰켓몬 종류를 담음
    
    if (len(nums_set) >= (len(nums)//2)): # 폰켓몬 N/2마리의 수보다 폰켓몬 종류의 수가 더 많거나 같으면 
        answer = len(nums)//2 # 폰켓몬 N/2마리의 수 출력
    else:                     # 그게 아니라 폰켓몬 종류보다 폰켓몬 N/2마리가 더 많거나 같으면
        answer = len(nums_set) # 폰켓몬 종류의 수 출력
    
    return answer

# 프로그래머스에선 처음 문제를 풀어봤는데, 백준과 스타일이 달라 조금 적응이 필요할 것 같다.
# 아직 def를 쓰는게 익숙치 않아 더 연습해야 할 것 같다

