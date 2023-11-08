def quickSort(P,S,first,last):
	if first >= last : return
	left , right = first+1,last
	p = P[first]/S[first]
	while left <= right:
		while left <= last and P[left]/S[left] > p:
			left += 1
		while right > first and P[right]/S[right] <= p:
			right -= 1
		if left <= right :
			P[left], P[right] = P[right], P[left]
			S[left], S[right] = S[right], S[left]
			left += 1
			right -= 1
	P[first], P[right] = P[right], P[first]
	S[first], S[right] = S[right], S[first]
	quickSort(P, S, first, right-1)
	quickSort(P, S, right+1, last)
	
def fractional_knapsack(n,S,P,K):
	if K <= 0: return 0
	s = 0
	p = 0
	selected_profit = 0
	for i in range(n):
		if s+S[i] <= K:
			selected_profit += P[i]
			s += S[i]
		else :
			selected_profit += (K-s)*(P[i]/S[i])
			s = K
			break
	return selected_profit

def Knapsack(i,T):
	global maxprofit
	global soultion 
	if i >= n or T <= 0:
		sol.pop(i-1)
		sol.insert(i-1,0)
		return 
	s, p = 0, 0
	if i == 0:
		s = 0
		p = 0
	else:
		for j in range(len(sol)):
			if sol[j] == 1:
				s+=S[j]
				p+=P[j]
	X[i]=1
	B = fractional_knapsack(n-(i+1),S[i+1:],P[i+1:],T-S[i])
	if s+S[i] <= K and (p+P[i]+B) > maxprofit:
		if (p + P[i]) > maxprofit:
			maxprofit = p + P[i]
		sol.pop(i)
		sol.insert(i,1)
		Knapsack(i+1, T-S[i])
	X[i]=0
	B = fractional_knapsack(n-(i+1), S[i+1:], P[i+1:], T)
	if p+B > maxprofit:
		sol.pop(i)
		sol.insert(i,0)
		Knapsack(i+1,T)
	return maxprofit

K = int(input())
n = int(input())
s = list(map(int, (input().split())))
p = list(map(int, (input().split())))
maxprofit = 0
sol = [0] * n
X = [0] * n
S = [0] * n
P = [0] * n
for i in range(n):
	S[i]=s[i]
	P[i]=p[i]
quickSort(P, S, 0, n-1)
print(Knapsack(0, K))