from time import time
alphabet = [
'',',','.','?','!',"'",':',';','-','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'0','1','2','3','4','5','6','7','8','9','\n','&',' ','—','(',')','"']
card = len(alphabet)
br = [0,0]
brs = [0,0]

def maxborderarray(s):
	n = len(s) - 1
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

def brst(s):
    n = len(s)-1
    i = 2
    while i < n:
        if s[br[i]+1] != s[i+1]:
            brs.append(br[i])
        else:
            brs.append(brs[br[i]])
        i += 1


def brsa_(s):
	brs.remove(0)
	m = len(s)
	brsa = [[0] * card for i in range(m)]
	for i in range(m):
		for j in range(card):
			if (brs[i]+1 >= m):
				continue
			else:
				if (s[brs[i]+1] == alphabet[j]):
					brsa[i][j] = brs[i]
				else:
					brsa[i][j] = brsa[brs[i]][j]
	return brsa

'''	
def kmp(t,p):
	n = len(t)
	m = len(p)
	k = 0
	s = ' ' + p + ' '
	maxborderarray(s)
	brst(s)
	#brsa = brsa_(p) 
	i = 0; q = 0
	while (i < n):
		while (q > 0 and p[q] != t[i]):
			q = brs[q]
		if (p[q] == t[i]):
			q += 1
		if (q == m):
			k += 1
			q = brs[m]
		i += 1
	return k
'''

def kmp(t,p):
	n = len(t)
	m = len(p)
	k = 0
	s = ' ' + p + ' '
	maxborderarray(s)
	brst(s)
	brsa = brsa_(p) 
	q = 0
	for i in range(n):
		if (q > 0 and p[q] != t[i]):
			x = alphabet.index(t[i])
			q = brsa[q][x]
		if (p[q] == t[i]):
			q += 1
		if (q == m):
			k += 1
			q = brs[m - 1]
	return k


filename = "T2.txt"
f = open(filename)
t = f.read()
for s in t:
	if (s not in alphabet):
		print("Текст содержит символы не принадлежащие алфавиту!")
		print(s)
		exit(0)
p = "ele"
for s in p:
	if (s not in alphabet):
		print("Образец содержит символы не принадлежащие алфавиту!")
		exit(0)
print("Текст T записан в файле: " + filename)
print("Искомый образец P: " + p)
print()
print("Алгоритм Кнута-Морриса-Пратта:")
t1 = time()
res = kmp(t,p)
t2 = time()
if (res == 0):
	print("Вхождений образца P в текст T не найдено!")
else:
	print("Кол-во вхождений образца P в текст T: " + str(res))
print("Время работы: " + str(t2 - t1) + " sec.")




