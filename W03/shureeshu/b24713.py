def heap_sort(A): # A[1..n]을 정렬한다.
    n = len(A)
    build_min_heap(A, n)
    for i in range(n-1,1,-1):
        swap(A[0], A[i])# 원소 교환
        heapify(A, 0, i - 1)
    print(-1)
    exit()
    
def build_min_heap(A, n): # type(A) = list, n = len(A)
    for i in range(n//2, 0, -1):
        heapify(A, i, n)

# A[k]를 루트로 하는 트리를 최소 힙 성질을 만족하도록 수정한다.
# A[k]의 두 자식을 루트로 하는 서브 트리는 최소 힙 성질을 만족하고 있다.
# n은 배열 A의 전체 크기이며 최대 인덱스를 나타낸다.

def heapify(A, k, n): # type(A) = list, n = len(A)
    left, right = 2*k + 1, 2*k + 2
    if right < n:
        if A[left] < A[right]:
            smaller = left
        else: smaller = right
    else:
        if left < n:
            smaller = left
        else: return # no child

    # 최소 힙 성질을 만족하지 못하는 경우 재귀적으로 수정한다.
    if A[smaller] < A[k]:
        swap(A[k], A[smaller])
        heapify(A, smaller, n)

def swap(a, b):
    global swap_cnt, k
    a, b = b, a
    swap_cnt += 1
    print(a, b)
    if swap_cnt == k:
        print(min(a, b), max(a, b))
        exit()

import sys
input = sys.stdin.readline
swap_cnt = 0
n, k = map(int, input().split())
A = list(map(int, input().split()))
heap_sort(A)

input_data = """5 2
2 5 1 4 3"""