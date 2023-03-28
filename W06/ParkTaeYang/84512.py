lst = ['','A','E','I','O','U']
# t = []
# t = set(t)
# for j in lst:
#     for k in lst:
#         for q in lst:
#             for p in lst:
#                 for w in lst:
#                     t.add((j+k+q+p+w).strip())
# t = list(t)
# t.sort()

# def solution(word):
#     for i in t:
#         if i == word:
#             return t.index(i)

# #시간복잡도는 list t의 n번 순회 O(N)

from itertools import product
t2 = []
t2 = set(t2)
for i in product(lst,repeat = 5):
    s = ''.join(i)
    t2.add(s)
t2 = list(t2)
t2.sort()
t2.pop()
print(t2)

#중복순열   t==t2

