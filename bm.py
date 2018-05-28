from time import time
alphabet = [
'',',','.','?','!',"'",':',';','-','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'0','1','2','3','4','5','6','7','8','9','\n','&',' ','—','(',')','"']
card = len(alphabet)
br = [0,0]
bl = []
bsuf = []
psuf = []


def maxborderarray(s):
	n = len(s)
	i = 1
	while i < n-1:
		t = br[i]
		while t > 0 and s[i+1] != s[t+1]:
			t = br[t]
		if s[i+1] == s[t+1]:
			br.append(t+1)
		else:
			br.append(0)
		i += 1

def cmp (s, p1, p2):
	n = len(s)
	c = 0
	t = 0
	if (p1 > n or p2 > n):
		return c
	else:
		if (n - p1 < n - p2):
			t = n - p1
		else:
			t = n - p2
		j = 0
		while (j < t and s[p1 + j] == s[p2 + j]):
			j += 1
		c = j
		return c

def blockarray(s):
	n = len(s)
	for j in range(n):
		bl.append(0)
	r = 0; l = 0;
	i = 1;
	while (i < n):
		bl[i] = 0
		if (i > r):
			bl[i] = cmp(s,0,i)
			if (bl[i] > 0):
				r = i + bl[i] - 1
				l = i
		else:
			k = i - l 
			if (bl[k] < r - i + 1):
				bl[i] = bl[k]
			else:
				bl[i] = r - i + 1
				l = i
				q = cmp(s,r-i+1,r+1)
				if (q > 0):
					bl[i] = bl[i] + q
					r = i + bl[i] - 1
		i += 1

def bsuf_(p):
	m = len(p)
	p2 = p[::-1]
	blockarray(p2)
	for i in range(m):
		bsuf.append(bl[m-i-1])

def psuf_(p):
	m = len(p)
	for i in range(m):
		psuf.append(0)
	for j in range(m):
		i = m - bsuf[j]
		if (i != m):
			psuf[i] = j

def shiftbadsymbol(p):
	m = len(p)
	bs = [[0] * m for i in range(card)]
	a = []
	for i in range(card):
		a.append(0)
	i = m - 1
	while (i >= 0):
		j = alphabet.index(p[i])
		bs[j][a[j]] = i
		a[j] += 1
		i -= 1
	return bs

'''
def shiftbadsymbol(p):
	bs = []
	m = len(p)
	for i in range(card):
		bs.append(0)
	for j in range(m):
		k = alphabet.index(p[j])
		bs[k] = j
	return bs
'''

'''
def badsymbol(t,p):
	n = len(t)
	m = len(p)
	bs = shiftbadsymbol(p)
	i = 0; k = 0
	while (i <= n-m):
		j = m - 1
		while(j >= 0 and p[j] == t[i+j]):
			j -= 1
		if (j == -1):
			k += 1
			i += 1
		else:
			i += max(1,j - bs[alphabet.index(t[i+j])])
	return k
'''

def badsymbol(t,p):
	n = len(t)
	m = len(p)
	bs = shiftbadsymbol(p)
	i = 0; k = 0
	while (i <= n-m):
		j = m - 1
		while(j >= 0 and p[j] == t[i+j]):
			j -= 1
		if (j == -1):
			k += 1
			i += 1
		else:
			q = 0
			w = alphabet.index(t[i+j])
			while (q <= bs[w][0] and bs[w][q] > j):
				q += 1
			i += max(1,j - bs[w][q])
	return k

'''
def badsymbol(t,p):
	n = len(t)
	m = len(p)
	maxborderarray(' ' + p)
	br.remove(0)
	bs = shiftbadsymbol(p)
	jump = 0
	i = 0
	k = 0
	while (i <= n-m):
		j = m - 1
		while(j >= jump and p[j] == t[i+j]):
			j -= 1
		if (j == jump - 1):
			k += 1
			if (br[m-1] == 0):
				i += 1
				jump = 0
			else:
				i += br[m-1]
				jump = m - br[m-1]
		else:
			i += max(1,j - bs[alphabet.index(t[i+j])])
			jump = 0
	return k
'''


filename = "T.txt"
f = open(filename)
t = f.read()
p = "ababaabbaababba"
res = badsymbol(t,p)
print(res)
bsuf_(p)
psuf_(p)
for elem in psuf:
	print(elem, end = ' ')


