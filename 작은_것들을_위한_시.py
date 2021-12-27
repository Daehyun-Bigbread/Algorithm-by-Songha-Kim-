def solve(A):
	n = len(A)
	S = []
	for i in range(n):
		S.append(A[i])
	extra = 0
	current = len(S)-1
	while current != extra:
		S.append(min(S[current], S[current-1]))
		current -= 1
		if (current-extra) == 0:
			extra += n
			n -= 1
			current = len(S)-1
	sum = 0
	for s in S:
		sum += s
	return sum
	# code here

A = [int(x) for x in input().split()]
print(solve(A))
'''
A값들을 새로운 dp테이블인 S에 저장하고 이미 저장되어 있는 끝을 current라고 하고 current에서부터 새로 저장되지 않은 마지막 부분인 extra까지 두개의 값씩 비교하며 최소값을 S에 저장한다. current와 extra의 값이 같으면 while문을 빠져나오고 마지막에 S값에 있는 값을 다 더해서 리턴한다.
시간복잡도는 O(n^2)이나 2차원배열을 사용하는것보다 빠르다.
'''
