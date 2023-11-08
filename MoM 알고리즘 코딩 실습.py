def find_median_five(A):
	B = []
	if len(A) == 0: return None
	for _ in range(len(A)):
		B.append(min(A))
		A.remove(min(A))
	return B[len(B)//2]
	
	
def MoM(A, k): # L의 값 중에서 k번째로 작은 수 리턴
	if len(A) == 1: # no more recursion
		return A[0]
	i = 0
	S, M, L, medians = [], [], [], []
	while i + 4 < len(A):
		medians.append(find_median_five(A[i: i+5]))
		i += 5
		
	if i < len(A) and i+4 >= len(A): # 마지막 그룹으로 5개 미만의 값으로 구성
		medians.append(find_median_five(A[i:]))

	mom = MoM(medians, int(len(medians)/2)+1)
	for v in A:
		if v < mom:
			S.append(v)
		elif v > mom:
			M.append(v)
		else:
			L.append(v)
	if len(S) >= k : return MoM(S, k)
	elif len(S) + len(L) < k: return MoM(M, k-(len(S)+len(L)))
	else: return mom

n, k = map(int, input().split())# n과 k를 입력의 첫 줄에서 읽어들인다
A = list(map(int, input().split()))# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
print(MoM(A, k))