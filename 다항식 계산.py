import time, random

def evaluate_n2(A, x):
	sum = 0
	for i in range(0, n):
		curr = 1
		for j in range(0, n):
			if i == j: break
			curr *= x
		sum += (A[i] * curr)
	return sum
	# code for O(n^2)-time function

def evaluate_n(A, x):
	curr = 1
	sum = 0
	for i in range(0, n):
		sum += (A[i] * curr)
		curr *= x
	return sum
	# code for O(n)-time function

random.seed() # random 함수 초기화
n = int(input()) # n 입력받음
A = [random.randint(-1000, 1000) for _ in range(n)]
x = random.randint(-1000, 1000)
# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
a = evaluate_n2(A, x)
b = evaluate_n(A, x)
# evaluate_n2 호출
# evaluate_n 호출
s1 = time.process_time()
c = evaluate_n2(A, x)
e1 = time.process_time()
print ("evaluate_n2 수행시간 =", format(e1 - s1, '.6f'))
s2 = time.process_time()
d = evaluate_n(A, x)
e2 = time.process_time()
print ("evaluate_n 수행시간 =", format(e2 - s2, '.6f'))
# 두 함수의 수행시간 출력