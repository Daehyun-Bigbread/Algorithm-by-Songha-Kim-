import heapq
	
def solve(A, k): # return k-th smallest key, 1 <= k <= n
	nums = []
	while A:
		nums.append(heapq.heappop(A))
	return nums[k-1]
k = int(input())
A = [int(x) for x in input().split()]
heapq.heapify(A) # A is now a min-heap
print(solve(A, k))
'''
주석

주어진 리스트를 heap으로 만들어준 후 solve 함수 내에서 heap sort를 해준다. 이때, 리스트를 새로 선언해주고 heap sort 된 리스트를 저장해준다. heap sort를 해준 리스트 num은 처음 주어진 리스트의 오름차순 정렬이 될 것이고 이때 (k - 1)번쨰 인덱스에 k번째로 작은 수가 저장되어 있으므로 num[k-1]을 리턴해준다.

주어진 방법은 heap sort를 이용하는데 평균적으로 O(nlogn)시간이 걸린다.

장점은 최적의 시간에 O(n)시간에 수행이 가능하다는 것과 평균 및 최악의 경우 수행시간이 O(nlogn)이어서 항상 O(nlogn) 시간에 문제를 풀 수 있다는 점이다.

단점은 실제 수행시간이 quick 정렬을 했을때보다 느리다. 데이터의 상태에 따라 다른 정렬법에 비해 수행시간이 느리다. 또한 Stable 하지 않다.

'''