# defaultdict ( default_factory=None , / [ , ... ] )

- 딕셔너리를 만드는 dict 클래스의 서브클래스
- 인자로 주어진 객체의 기본값을 딕셔너리값의 초기값으로 지정할 수 있다.
- 숫자, 리스트, 셋 등으로 초기화할 수 있기때문에 여러 용도로 사용가능

- [참고1](https://appia.tistory.com/218)
```python
normalDict = {}
normalDict.setdefault("V", 0)
print(normalDict)
# result 
{'V': 0}
```
```python
normalDict = {}
normalKey =["A","B","C"]
for item in normalKey:
  normalDict.setdefault(item, 0)
print(normalDict)
# result
{'A': 0, 'B': 0, 'C': 0}
```
=> 함수를 매번 호출해야하기 때문에 속도면에서 효율성 떨어짐

```python
from collections import defaultdict
normalDict = defaultdict(int)
normalKey =["A","B","C"]
for item in normalKey:
  normalDict[item]
print(normalDict)
# result
defaultdict(<class 'int'>, {'A': 0, 'B': 0, 'C': 0})
```
=> int를 인자로 넣으면 기본값이 0이 됨

```python
from collections import defaultdict
normalDict = defaultdict(int)
print(normalDict)
normalDict["a"]
print(normalDict)
normalDict["v"]
print(normalDict)
# result
defaultdict(<class 'int'>, {})
defaultdict(<class 'int'>, {'a': 0})
defaultdict(<class 'int'>, {'a': 0, 'v': 0})
```
=> 최초에 없는 키값들을 입력해도 에러가 나지 않고, 설정된 값으로 초기화 됨, 자동 추가

- [참고2](https://docs.python.org/3/library/collections.html#collections.defaultdict)
```python
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
  d[k].append(v)
sorted(d.items())
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```
```python
s = 'mississippi'
d = defaultdict(int)
for k in s:
  d[k] += 1
sorted(d.items())
# [('i', 4), ('m', 1), ('p', 2), ('s', 4)]
```
```python
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
  d[k].add(v)
sorted(d.items())
# [('blue', {2, 4}), ('red', {1, 3})]
```