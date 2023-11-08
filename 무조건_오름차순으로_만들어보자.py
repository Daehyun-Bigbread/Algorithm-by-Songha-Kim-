INF = int(1e9)
def solve(A):
	n = len(A)
	max_num = max(A)
	min_num = min(A)

	S = [[0 for _ in range(max_num+1)] for _ in range(n)]

	for i in range(min_num, max_num+1):
		S[0][i] = abs(A[0]-i)
	for i in range(1, n):
		minimum = INF
		for j in range(min_num, max_num+1):
			minimum = min(minimum, S[i-1][j])
			S[i][j] = minimum + abs(A[i]-j)
	ans = INF
	for i in range(min_num, max_num+1):
		ans = min(ans, S[n-1][i])
	return ans
	# code here

A = [int(x) for x in input().split()]
print(solve(A))
'''
dp테이블인 S를 만들어주고, 처음 for문으로 base case들에 대해 새로운 테이블인 S를 채운다. S(i, j)는 i번째 요소가 j인 경우 배열을 만드는 데 필요한 최소 연산 수이다. (i-1)번째 값을 사용하여 i값을 채워준다. 만약 i번째 요소가 j이면 i-1번째 요소로 min_num부터 j 값까지 가질 수 있다. 값들 중 최소값을 S에 저장한다. 마지막 for문에서 min_num부터 max_num까지 S[n-1][j]값들중 최소값을 찾아 return 해준다.
시간복잡도는 O(n*k)인데, 이 때의 k는 (max_num-min_num+1)이다
'''