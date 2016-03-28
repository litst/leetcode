def f(k,n,step,curSet):
	if step == k:
		if sum(curSet) == n:
			ans.append(curSet)
		else:
			return
	else:
		for i in xrange(curSet[-1]+1,10):
			f(k,n,step+1,curSet+[i])

ans = []
k = 3
n = 9
for i in xrange(1,10):
	f(k,n,1,[i])
print ans