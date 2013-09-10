import sys
from collections import defaultdict

def isOK(table, names):
	for p in names:
		for q in names:
			if q in graph[p]:
				return False
	return True

T = int(sys.stdin.readline())

for i in range(T):
	N = int(sys.stdin.readline())

	graph = defaultdict(set)
	A = set()
	B = set()
	
	for j in range(N):
		name1, name2 = sys.stdin.readline().strip().split()
		graph[name1].add(name2)
		graph[name2].add(name1)
		if j == 0:
			A.add(name1)
			B.add(name2)
	
	for j in range(N):
		for a in A:
			B.update(graph[a])
		for b in B:
			A.update(graph[b])

	result = isOK(graph, A) and isOK(graph, B)

	print 'Case #%d: %s' % (i + 1, result and 'Yes' or 'No')


		
