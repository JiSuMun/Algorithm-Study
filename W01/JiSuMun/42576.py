# 해시
# 완주하지 못한 선수
# 시간복잡도: Counter => O(N), 딕셔너리에서 원소 접근할때: O(1)
from collections import Counter
def solution(participant, completion):
    res = Counter(participant) - Counter(completion)
    return list(res.keys())[0]

"""
같은 것은 모두 사라지고 겹치지 않는 것만 남으면 됨.
이 경우에도 같은 이름이 2개 이상 나오면 복잡하게 됨.
그래서 Counter 클래스 사용해서 이름과 빈도수를 딕셔너리로 저장한 다음,
차를 구하면 완주하지 못한 선수의 이름과 빈도수가 나옴.
return 할 때, 리스트로 만들지 않고 출력했다가 오류나옴
"""