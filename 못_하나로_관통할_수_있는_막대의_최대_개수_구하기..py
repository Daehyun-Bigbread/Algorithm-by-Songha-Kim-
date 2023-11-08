INF = int(200000)
n = int(input())
A = [0]*n

for i in range(n):
	A[i] = list(map(int, input().split()))
A = sorted(A, key = lambda x :(x[1], x[0]))

def solve(A):
	S = [0 for _ in range(INF)]
	for i in range(0, n):
		S[A[i][0]] += 1
		S[A[i][1]+1] -= 1
	temp = S[0]
	for i in range(1, INF):
		S[i] += S[i-1]
		if (temp < S[i]):
			temp = S[i]
	return max(S)

print(solve(A))
'''
dp테이블인 S를 만들어서 막대가 시작되는 부분은 +1을 해주고 끝나는 부분은 -1을 해준다.
S를 prefix sum하여 제일 큰 값을 리턴해준다.
시간복잡도는 O(n+INF)가 된다.
'''