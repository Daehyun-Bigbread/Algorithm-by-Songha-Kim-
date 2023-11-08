n = int(input())
A = [0]*n

for i in range(n):
	A[i] = list(map(int, input().split()))

def solve(A):
	A = sorted(A, key = lambda x :(x[1], x[0]))
	temp = A[0][1]
	pin = 1
	for i in range(1,n):
		if A[i][0] > temp:
			pin += 1
			temp = A[i][1]
	return pin
print(solve(A))

'''
입력받은 막대를 좌표 기준으로 정리해주고 리스트를 돌아가면서 현재 좌표보다 작은 값을 센다.
수행시간은 O(n)이 된다.
'''