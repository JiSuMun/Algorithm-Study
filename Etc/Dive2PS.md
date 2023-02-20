# Dive to PS : 2023.02.18

## 반드시 알아야하는 라이브러리
1. built-in (내장 함수)
input(), print()
sum(), min(), max()
eval()
sorted()
1. itertools
순열과 조합
class : permutaions, combinations, product, combination_with_replacement
1. heapq
O(NlogN) 의 sorting 
1. bisect
O(logN)의 탐색
function : bisect_left(), bisect_right(), count_by_range()
1. collections
유용한 자료구조의 제공
class : deque, Counter
1. math
자주 사용되는 수학적인 기능 (팩토리얼, 제곱근, 최대공약수)
function : factorial(), sqrt(), gcd(a, b)
constant : pi, e

## exception

## 시간 복잡도
- 만약 소스코드가 내부적으로 다른 함수 를 호출한다면 내부 함수의 시간 복잡도까지 고려해야 한다.
- 일반적으로 코딩 테스트에서는 최악의 경우에 대한 연산 횟수가 가장 중요하다. 그러니 최악의 경우의 시간 복잡도를 우선적으로 고려해야 한다.
- 보통 시간 복잡도에서의 ‘연산’은 프로그래밍 언어에서 지원하는 사칙 연산, 비교 연산 등과 같은 기본 연산을 의미한다. 예를 들어 두 정수 a와 b를 더하는 더하기 연산뿐만 아니라, 두 정수 a와 b의 값을 비교하는 비 교 연산 또한 한 번의 연산으로 취급한다
- 알고리즘 대회 참가에 익숙한 사람들은 문제의 조건을 확인한 뒤에 사용할 수 있는 알고리즘을 좁혀 나가는 전략을 채택하기도 한다.
- 프로그래밍 테스트에서 문제를 풀 때는 가독성을 해치지 않는 선에서 최대한 복잡도가 낮게 프로그램을 작성해야 한다.
- 일반적으로 코딩 테스트 환경에서는 O(N 3)을 넘어가면 문제 풀이에서 사용하기 어렵다. 왜냐하면 CPU 기반의 개인 컴퓨터나 채점용 컴퓨터에서는 연산 횟수가 10억을 넘어가면 C 언어를 기준으로 통상 1초 이상의 시간이 소요된다. 이때 N의 크기가 5,000이 넘는다면 족히 10초 이상의 시간이 걸릴 수 있다. 특히 파이썬은 더욱 오래 걸리며, 코딩 테스트 문제에서 시간 제한은 1 ~ 5초가량이 므로 보통 연산 횟수가 10억을 넘어가도록 작성하면 오답 판정을 받을 수 있다.

시간 제한이 1초 일 때
- N의 범위가 500인 경우: 시간 복잡도가 O(N3)인 알고리즘을 설계하면 문제를 풀 수 있다. 
- N의 범위가 2,000인 경우: 시간 복잡도가 O(N2)인 알고리즘을 설계하면 문제를 풀 수 있다. 
- N의 범위가 100,000인 경우: 시간 복잡도가 O(NlogN)인 알고리즘을 설계하면 문제를 풀 수 있다. 
- N의 범위가 10,000,000인 경우: 시간 복잡도가 O(N)인 알고리즘을 설계하면 문제를 풀 수 있다.

N이 1,000일 때의 연산 횟수
- O(N) : 1,000
- O(NlogN) : 10,000
- O(N^2) : 1,000,000
- O(N^3) : 1,000,000

- 코딩테스트에는 시간 제한(효율성)이 존재하기 때문에 시간복잡도가 매우 중요하다.만약 문제에서 주어진 N이 10,000 이라면 O(N^3) 풀이 방법으로는 시간 초과가 날 것이다. (대부분의 테스트 환경에서) 반대로 생각하면, 이것은 문제의 힌트와 같다! 시간복잡도를 고려하여 제한 시간내 성공 가능한 알고리즘이 문제의 정답이기 때문이다.따라서 자료구조, 알고리즘의 시간복잡도는 반드시 알아야 한다.

- [파이썬: 자료형 별 연산자의 시간복잡도(Big-O) 정리_Dev JaykO](https://duri1994.github.io/python/algorithm/python-time-complexity/)

## 공간 복잡도
- 코딩 테스트에서는 보통 메모리 사용량을 128 ~ 512MB 정도로 제한한다. 다시 말해 일반적인 경 우 데이터의 개수가 1,000만 단위가 넘어가지 않도록 알고리즘 설계를 해야 한다.

## 수행 시간 측정 소스코드 
```python 
import time 

start_time = time.time() # 측정 시작

# 프로그램 소스코드 

end_time = time.time() # 측정 종료 

print("time :", end_time - start_time) # 수행 시간 출력
```
- 자신이 설계한 알고리즘의 성능을 실제로 확인하기 위해서, 시간 측정 라이브러리를 사용해보는 습관을 기르는 것이 좋다.

## 주요 알고리즘 이론
- 그리디, 구현, DFS/BFS, 정렬, 이진 탐색, 다이나믹 프로그래밍, 최단 경로, 그래프 이론

## 기타 알고리즘
- 소수 판별법 : 에라토스테네스의 체
- 투 포인터 : 투 포인터 알고리즘은 '정렬되어 있는 두 리스트의 합집합' 같은 문제에 효과적으로 사용활 수 있으며, 병합 정렬에도 사용되고 있다.
- 구간 합 계산 : 항상 우리가 알고리즘을 설계할 때 고려해야 할 점은, 여러 번 사용될 만한 정보는 미리 구해 저장해 놓을수록 유리하다는 것이다. 구간 합 계산을 위해 가장 많이 사용되는 기법이 바로 접두사 합Prefix Sum이다. 각 쿼리에 대해 구간 합을 빠르게 계산하기 위해서는 N개의 수의 위치 각각에 대하여 접두사 합을 미리 구해 놓으면 된 다. 여기에서 접두사 합이란 리스트의 맨 앞부터 특정 위치까지의 합을 구해 놓은 것을 의미한다.
- 순열과 조합 : 순열과 조합은 실제 코딩 테스트에서 필요한 경우가 많기 때문에, 어떻게 사용할 수 있는지를 알고 있어야 한다. 사실 순열과 조합은 재귀 함수 혹은 반복문을 이용해서 직접 구현할 수도 있지만, 실제 코딩 테스트에서 이를 직접 구현하는 것은 매우 번거롭다. 경우의 수를 계산할 경우 *_ nPr = n!/(n-r)! _*, *_ nCr = n!/r! x (n-r)! _* 모든 경우(사건)을 다 출력하도록 요구할 경우 : `itertools` 라이브러리를 사용한다.

### 기타 알고리즘 예제
소수구하기 1929
암호만들기 1759

# 팁
- 

## 출제 경향

- 가장 출제 빈도가 높은 문제는 그리디Greedy, 구현Implementation, DFS/BFS를 활용한 탐색 문제이다.
- 구현 문제는 실제 개발 과정에서 사용될 법한 구현 기법들을 물어보는 경우가 많다.
- 상대적으로 높은 사고력을 요구하는 다이나믹 프로그래밍이나 그래프 이론 문제도 출제된다. 다만, 이런 유형의 문제는 출제되더라도 난이도가 높지 않은 경향이 있다.

- 대부 분의 알고리즘 대회 및 코딩 테스트에서는 상위 5% 미만의 사람만 문제를 전부 풀 수 있으며*** 전체 문제 중에서 절반가량을 정확히 해결할 수 있다면 합격할 수 있다.
- 합격자는 평균 69%의 문제를 풀었으며, 불합격 자는 평균 38%의 문제밖에 풀지 못했다고 응답했다.

- 코드포스 블루* 이상, ACM-ICPC 서울 지역 대회 본선에 안정적으로 진 출할 수 있는 응시자는 삼성전자, 카카오, 라인 모두 합격권에 있다.
- 기업 코딩 테스트에서는 대회 입상을 목 표로 하는 사람들이 학습해야 하는 고난이도 알고리즘을 주로 다루지는 않는다.

- 알고리즘 문제 를 푸는 것도 중요하지만, 이후 기술 면접에서 잘 대답하려면 문제 접근 방식과 풀이 방식을 설명할 수 있어야 한다.
- 어떤 상황 에 어떤 알고리즘을 사용하는지 잘 익혀두자.
- 단순히 어떤 정렬 라이브러리의 시간 복잡도가 높다, 낮다를 판단하는 것만으로는 부족하고, 실제로 서 로 다른 알고리즘을 비교하여 ‘특정한 상황’에서 무엇이 더 좋을지를 설명할 수 있어야 한다.

- 국내 기술 면접에 대한 전반적인 내용을 정리한 ‘국내 기술 면접 가이드라인’ 저장소가 있으니 기 술 면접 전에 읽어보자. 분야별로 알아두어야 하는 내용이 정리되어 있다. [국내 기술 면접 가이드라인](https://github.com/JaeYeopHan/Interview_Question_for_Beginner)

- 기업은 자신이 어떤 방법으로 문제 에 접근하여 어떠한 알고리즘을 사용했는지를 논리 정연하게 설명할 수 있는 지원자를 원한다.논리적으로 말로 정리하는 능력도 매우 중요하다. 이러한 능력은 하루아침에 생기는 게 아니므로 평소에 기술 블로그나 깃허브 저장소를 운영 하며 능력을 키워갈 수 있다. 또한 글로도 논리적인 풀이 능력을 확인할 수 있으므로 채용 시 장점이 될 수도 있다.

- 외국계 기업에 취업하려는 취업 준비생이나 국제 알고리즘 대회를 준비하는 학생은 소개하는 해외 알고리즘 문제 풀이 사이트를 이용하는 것을 추천한다. 당연히 국제 대회를 준비한다면 영어 문제를 해석하는 능력 또한 필요하다. 이런 연습은 후에 영어로 쓰인 개발 문서를 읽는 데에도 도움이 될 것이다.

[코딩테스트 문제 유형 정리_ilhwanee's devlog](https://velog.io/@pppp0722/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%AC%B8%EC%A0%9C-%EC%9C%A0%ED%98%95-%EC%A0%95%EB%A6%AC)

1. 브루트 포스(완전탐색)

코딩테스트 필수 of 필수일 만큼 자주 출제되는 유형으로 완탐이라고 줄여 부르기도 한다. DFS, BFS, 백트래킹(완탐은 아니긴 하다)을 공부하자. 이름 그대로 모든 경우를 탐색해야 할 경우에 사용된다. (미로찾기 등) 무작정 모든 경우를 탐색하면 효율이 낮으므로, 시간 제한에서 실패하면 다른 풀이를 생각해보거나 문제 조건에 따라 탐색을 최소한으로 만들어야 한다.

1. 다이나믹 프로그래밍

복잡한 문제를 한 번에 해결하는 것이 아닌, 조금씩 점차적으로 풀이하는 유형이다. (점화식을 떠올리면 이해하기 쉬움)
개인적으로 어려운 유형이라고 생각한다.다른 유형도 그렇겠지만, 특히 DP는 여러 문제를 풀어보면서 감을 익혀보자.bottom-up, top-down 을 모두 공부하자. (필자는 bottom-up 접근이 편하다고 생각) 한 문제를 bottom-up, top-down 두 방법으로 각각 풀이해보는 것도 좋다.

1. 그리디

부분적인 최적해가 전체적인 최적해가 되는 문제에서 사용한다.
어렵게 출제되면 풀이를 쉽게 떠올리기 힘드니, 문제를 많이 풀어보면서 풀이 방법을 기억하자.
우선순위 큐를 활용하는 경우가 많다.

1. 이분 탐색

순차적인 배열 탐색으로 시간 초과가 나면 떠올리자.
시간 복잡도 : O(logN)로 그냥 순회하는 O(N)보다 빠르다.
이분 탐색 + 다익스트라 등 다른 유형과 연계되는 문제가 출제될 수 있다.

1. 그래프

최단 경로를 구하는 문제가 많이 출제된다.
최단 경로를 구할 때는 다익스트라, 벨만-포드, BFS, 플로이드-워셜 알고리즘들을 사용하자.
그래프 순회에는 DFS / BFS를 사용하자.
추가로 학습하면 좋은 알고리즘으로는 위상정렬이 있다.

1. 투 포인터, 슬라이딩 윈도우

배열에서 인덱스 2개를 사용해야 할때 평범하게 for 문 2번으로 풀이하면 시간 초과가 발생하는 경우 생각해볼 수 있다.
인덱스 2개를 for 문 한번으로 사용하면서 문제를 해결할 수 있다.
구간 합도 공부하자.

1. 유니온 파인드

최근 자주 기출되는 유형이다.
노드를 집합에 속하게 하는 Union 연산과 노드의 루트 노드를 찾는 Find 연산으로 이루어진다.
노드들을 루트 노드를 기준으로 하는 어떠한 집합으로 묶는다고 생각하면 이해하기 편하다.

1. 최소 신장 트리

최소 신장 트리를 만드는데 필요한 비용을 구하는 유형이다.
자주 기출되지는 않지만, 사용되는 알고리즘이 어렵지 않으니 익혀두자.
크루스칼, 프림 알고리즘을 공부하자.


- 알고리즘 문제 풀이 사이트 (백준과 프로그래머스만 활용한다면 많은 기업의 코딩 테스트를 커버할 수 있다.)
1. 입문자 추천 : [코드 시그널](https://app.codesignal.com), [게임코딩](https://www.codingame.com)
1. [코딩도장](https://codingdojang.com)
1. [정올](https://www.jungol.co.kr)
1. [백준](https://www.acmicpc.net/)
1. [코드업](https://codeup.kr/)
1. [프로그래머스스쿨](https://school.programmers.co.kr/) : 취업 준비에 특화된 문제, SQL 문제 보유, 모의 코딩테스트 가능, 카카오 코딩 테스트
1. [SWEA](https://swexpertacademy.com/)
1. [네이버엘리스](https://academy.elice.io/)
1. [구름DEVTH](https://devth.goorm.io/) : NHN, 우아한형제들, 라인플러스
1. [구름LEVEL](https://level.goorm.io/)
1. [알고스팟](https://algospot.com/) : 종만북 사용시 필수 사이트

- 외국 사이트
1. [코딜리티](https://app.codility.com/programmers/trainings/) : 네이버, 우아한형제들, 이스트소프트, 야놀자
1. [탑코더](https://www.topcoder.com/community/arena) : 알고리즘 경진대회를 격주마다 개최
1. [코드포스](https://codeforces.com) : 양질의 문제, 영어와 러시아어만 지원, 온라인 경진대회에 참가하여 블루 이상을 노려보자 !
1. [해커랭크](https://www.hackerrank.com/) : SQL 문제 보유
1. [릿코드](https://leetcode.com/) : Weekly Contest 온라인 대회 개최, 이 사이트의 hard문제를 풀 수 있어야 구글에 들어갈 수 있다, 프리미엄 계정을 구매하면 FAANG 인터뷰 기출도 확인할 수 있다. 블랙프라이데이 시즌 때 프리미엄 계정을 할인 판매한다
1. [코더바이트](https://coderbyte.com/) : 해외 코딩 인터뷰 준비 사이트 (유료)
1. [AtCoder](https://atcoder.jp/): 매주 코딩테스트 실시
1. [구글코드잼](https://codingcompetitions.withgoogle.com/codejam/) : 제일 유명한 코딩테스트(1년 1번)
1. [구글해시코드](https://codingcompetitions.withgoogle.com/hashcode) : 각종 np 문제로 매년 가장 최적화 한 팀을 뽑는 대회(팀단위 참가 가능)

- 기타
1. [스피드코더](https://www.speedcoder.net/) : 프로그래머를 위한 타자연습 사이트
1. [프로젝트오일러](https://euler.synap.co.kr/) : 수학적인 문제 특화
1. [codewars](https://www.codewars.com/)
1. [CodinGame](https://www.codingame.com/start)
1. [코드그라운드](https://www.codeground.org/) : 삼성 프로그래밍 경시대회 문제 모음집 SCPC, 코드 그라운드는 기업의 코딩 테스트를 위한 사이트이기 보다는 알고리즘 및 코딩 대회를 참가하기 위한 곳이다.
1. [코이스터디](http://koistudy.net/)

- 참고하기 좋은 사이트
1. [Geeksforgeeks](https://www.geeksforgeeks.org/)
1. [Algorithms for Competitive Programming](https://cp-algorithms.com/)
1. [동빈나 깃헙](https://github.com/ndb796) : 이코테 책의 문제를 풀다 막힐 때 저자에게 질문 가능
1. [동빈나 알고리즘 팀 노트](https://github.com/ndb796/Python-Competitive-Programming-Team-Notes)

- 레퍼런스
1. [이것이 코딩 테스트다](https://github.com/ndb796/python-for-coding-test)
1. [코딩테스트 준비 사이트 모음집(단순링크만)_태빵.log](https://velog.io/@jeon3029/코딩테스트-준비-사이트-모음집단순링크만)
1. [코딩테스트 연습 사이트 10개 추천 ( 온라인, 외국 )](https://toptrend.blog/코딩테스트-연습-사이트)
1. [코딩테스트 문제 유형 정리_ilhwanee's devlog](https://naver.me/x4aEAfK0)

- 뉴스/소식
1. [TechBlogPosts](https://techblogposts.com/) : 여러 기업의 기술 블로그 새 포스팅을 볼 수 있는 사이트
1. [codenary](https://www.codenary.co.kr/techblog/list) : 스타트업들의 기술 블로그를 볼 수 있는 사이트

- 파이썬 관련
1. [파이썬 공식 문서](https://docs.python.org/ko/3/index.html)
  - [Built-in Functions](https://docs.python.org/3/library/functions.html#built-in-funcs)
  - [Built-in Constants](https://docs.python.org/3/library/constants.html#built-in-consts)
  - [Standard Library](https://docs.python.org/ko/3/library/index.html)
  - [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
1. [귀도의 1991년 페이퍼](https://ir.cwi.nl/pub/18204)

## Built-in Functions

`all(_iterable_)` : return `True` if all elements of the _iterable_ are true(or if the iterable is empty).
`any(_iterable_)` : return `True` if any elements of the _iterable_ is true. If the iterable is empty, return `False`.
