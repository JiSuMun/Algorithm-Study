def solution(nums):
    dic = {}
    for i in nums:
        dic[i] = dic.get(i,0)+1      
        # 리스트를 딕셔너리 형식으로 만들어주기

    # 리스트 길이의 절반만큼 뽑을때
    if len(dic)>=len(nums)//2:       
        answer = len(nums)//2        
        # 딕셔너리의 크기가 뽑는수보다 많다면 나오는 최대의 경우의수는 뽑는것을 모두다르게 => 뽑는 개수
    else:
        answer = len(dic)            
        # 딕셔너리의 크기가 뽑는수보다 작다면 최대의 경우는 모든 딕셔너리에서 하나씩 뽑은 후 
        # 나머지는 아무거나 뽑기 => 딕셔너리의 개수 
    return answer