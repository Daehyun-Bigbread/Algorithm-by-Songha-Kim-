def merge(A, i, j, k, l):
	# i <= j and j < k <= l
	# 정렬된 두 부분 A[i..j]와 A[k..l]을 merge하는 함수
	first = i
	last = l
	B = []
	while i <= j and k <= l:
		if A[i] <= A[k]:
			B.append(A[i])
			i += 1
		else:
			B.append(A[k])
			k += 1
	for i in range(i, j+1): B.append(A[i])
	for j in range(k, l+1): B.append(A[j])
	for k in range(first, last+1): A[k] = B[k-first]

def m_sort(A, first, last):
	# 3-way merge sort - merge 함수를 이용해 적절히 합병한다
	if first >= last: return
	else:
		j = first + ((last-first)//3)
		k = first + 2*((last-first)//3)

		m_sort(A, first, j)
		m_sort(A, j+1, k)
		m_sort(A, k+1, last)

		return merge(A, first, j, j+1, k), merge(A, first, k, k+1, last)

def check(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return A[0]+A[(len(A)//2)]+A[-1]

A = [int(x) for x in input().split()]
m_sort(A, 0, len(A)-1)
print(check(A))