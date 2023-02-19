# def solution(phone_book):
#     p = len(phone_book)
#     for i in range(p-1):
#         for j in range(i+1,p):
#             t = min(len(phone_book[i]),len(phone_book[j]))
#             for k in range(t):
#                 if phone_book[i][k] != phone_book[j][k]:
#                     break
#             else:
#                 return False                   
#     else:
#         return True

# 시간초과 91.7 / 100.0

# 3번과 4번 라인의 이중반복문으로 복잡도 O(n^2)으로 인한 시간초과


def solution(phone_book):
    phone_book = sorted(phone_book)                         
    #리스트를 정렬
    p = len(phone_book)
    for i in range(p-1):
        t = min(len(phone_book[i]),len(phone_book[i+1]))        
        #둘중 작은 값만큼 순회
        for k in range(t):
            if phone_book[i][k] != phone_book[i+1][k]:          
                break
                #문자열 형태로 정렬했기때문에 i번쨰를 모두와 비교할 필요없이 i+1번째만 비교
        else:
            return False                   
    else:
        return True


# 통과

# 시간복잡도는 sorted를 사용했기에 O(nlogn)