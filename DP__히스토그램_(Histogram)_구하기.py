INF = float(1e9)
S = [[INF for _ in range(31)] for _ in range(1001)]

def solve(n, k):
	if n <= k:
		return 0.0
	if S[n][k] != INF:
		return S[n][k]
	if k == 1:
		m = sum1[n]/n
		temp = m*m*n-2*m*sum1[n]+sum2[n]
		S[n][k] = temp
		return temp
	temp = INF
	for i in range(n, k-1, -1):
		m = (sum1[n]-sum1[i-1])/(n-i+1)
		temp = min(temp, solve(i-1,k-1)+m*m*(n-i+1)-2*m*(sum1[n]-sum1[i-1])+sum2[n]-sum2[i-1])
	S[n][k] = temp
	return temp


k, n = map(int, input().split())
sum1 = [0 for _ in range(n+1)]
sum2 = [0 for _ in range(n+1)]
for i in range(1, n+1):
	num = float(input())
	sum1[i] = sum1[i-1]+num
	sum2[i] = sum2[i-1]+num*num
print(round(solve(n, k),3))

'''
오차는 분산에 크기만큼을 곱한것과 같다.
쉽게 분산을 구하기 위해서 제곱의 평균에서 평균의 제곱을 빼는 식을 생각하여
sum1, sum2에 각각 합과 제곱의 합을 저장한다.(누적으로 저장한다.)
이렇게 하면 O(1)시간에 분산을 계산할 수 있게 된다.
S[i][j]를 계산해주기 위해서는 j-1보다 크고 i보다 작은 k에 대하여
S[k][j-1]에 오차를 더한 값과 현재값 중 작은 값을 택하면 된다.

코드의 시간복잡도는 그룹수를 b, 크기를 n이라 하면 O(n^2*b)가 된다.
'''