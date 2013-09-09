import sys

iibbb;
aaaa;

def calc(names):
	count = 0
	lastName = names[0]
	for i in range(1, len(names)):
		if lastName > names[i]:
			count += 1
		else:
			lastName = names[i]
	return count

T = int(sys.stdin.readline())
for i in range(T):
	N = int(sys.stdin.readline())

	names = []
	for j in range(N):
		names.append(sys.stdin.readline().strip());

	print 'Case #%d: %d' % (i + 1, calc(names))

