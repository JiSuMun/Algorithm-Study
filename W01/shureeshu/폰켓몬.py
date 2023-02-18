# 폰켓몬

# 시간복잡도 : O(N)
# 공간복잡도 : 

def solution(nums):
    num_choose = len(nums)//2 # 1
    num_kinds = len(set(nums)) # N
    answer = min(num_choose, num_kinds) # 1
    return answer

"""

my폰켓몬 = {선택 1, 선택 2, ... 선택 len(nums)//2}
가질 수 있는 종류의 최대값 = len(set(my포켓몬)) <= len(my폰켓몬) = len(nums)//2
조건 1: answer <= len(nums)//2

주어진 포켓몬 종류의 수 = len(set(nums))
조건 2: 가질 수 있는 종류의 최대값 <= len(set(nums))

∴ answer = min(num_choose, num_kinds)

"""
# 제한 사항
# nums는 폰켓몬의 종류 번호가 담긴 1차원 배열입니다.
# nums의 길이(N)는 1 이상 10,000 이하의 자연수이며, 항상 짝수로 주어집니다.
# 폰켓몬의 종류 번호는 1 이상 200,000 이하의 자연수로 나타냅니다.
# 가장 많은 종류의 폰켓몬을 선택하는 방법이 여러 가지인 경우에도, 선택할 수 있는 폰켓몬 종류 개수의 최댓값 하나만 return 하면 됩니다.

# len(s)
# 객체의 길이 (항목 수)를 돌려줍니다. 인자는 시퀀스 (문자열, 바이트열, 튜플, 리스트 또는 range 같은) 또는 컬렉션 (딕셔너리, 집합 또는 불변 집합 같은) 일 수 있습니다.

# 시퀀스 형
# 기본 시퀀스 형 — list, tuple, range
# 바이너리 시퀀스 형 — bytes, bytearray, memoryview
# 텍스트 시퀀스 형 — str

# Concatenating immutable sequences always results in a new object. This means that building up a sequence by repeated concatenation will have a quadratic runtime cost in the total sequence length. To get a linear runtime cost, you must switch to one of the alternatives below:

# if concatenating str objects, you can build a list and use str.join() at the end or else write to an io.StringIO instance and retrieve its value when complete

# if concatenating bytes objects, you can similarly use bytes.join() or io.BytesIO, or you can do in-place concatenation with a bytearray object. bytearray objects are mutable and have an efficient overallocation mechanism

# if concatenating tuple objects, extend a list instead

# for other types, investigate the relevant class documentation

# sequence (시퀀스)¶
# __getitem__() 특수 메서드를 통해 정수 인덱스를 사용한 빠른 요소 액세스를 지원하고, 시퀀스의 길이를 돌려주는 __len__() 메서드를 정의하는 이터러블. 몇몇 내장 시퀀스들을 나열해보면, list, str, tuple, bytes 가 있습니다. dict 또한 __getitem__() 과 __len__() 을 지원하지만, 조회에 정수 대신 임의의 불변 키를 사용하기 때문에 시퀀스가 아니라 매핑으로 취급된다는 것에 주의해야 합니다.

# collections.abc.Sequence 추상 베이스 클래스는 __getitem__() 과 __len__()을 넘어서 훨씬 풍부한 인터페이스를 정의하는데, count(), index(), __contains__(), __reversed__()를 추가합니다. 이 확장된 인터페이스를 구현한 형을 register()를 사용해서 명시적으로 등록할 수 있습니다.

# set()
# Time Complexity: Set method is implemented as a hash table, so the time complexity is O(1)
