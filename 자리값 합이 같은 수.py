import sys
sys.setrecursionlimit(10000)
def count(L, S):
	if (L == 0):
		return S == 0
	if (dp[L][S] != -1):
		return dp[L][S]
	ans = 0
	for i in range(10):
		if (S-i >= 0):
			ans += count(L-1, S-i)
	dp[L][S] = ans
	return dp[L][S]

def solve(L, S):
	ans = 0
	for i in range(1, 10):
		if (S - i >= 0):
			ans += count(L-1, S-i)
	return ans

L, S = [int(x) for x in input().split()]
dp = [[-1 for i in range(1000)] for i in range(1000)]
print(solve(L, S)%2147483647)

'''
0으로 채우면 timeout 에러가 나서 -1로 dp 테이블을 채워준다.
count함수는 이미 dp테이블에 값이 저장되어있으면 그 값을 리턴해주고
아니면 새로 값을 저장해주는 역할을 한다.
solve 함수는 반환받은 값들을 다 저장해서 갯수가 몇개인지 리턴해주는 함수이다.
처음 dp테이블을 채워주는데 O(n^2)이 걸리고 수행시간은 O(S)시간으로 풀수있다.
'''





