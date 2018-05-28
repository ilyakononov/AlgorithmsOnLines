from time import time
symbol = '$'
br = [0,0]
bl = []

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

'''
def maxborder(s):
	n = len(s)
	maxbr = 0
	count = n - 1
	i = 1
	while (i <= count):
		j = n - i 
		if (s[:i] == s[j:]):
			maxbr = i
		i+=1
	return maxbr

def maxborderarray(s):
	n = len(s)
	count = n -1
	i = 1
	while (i <= count):
		br.append(maxborder(s[:i]))
		i+=1
	br.append(maxborder(s[:]))
'''

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


'''
def block(s):
	n = len(s)
	for j in range(n):
		bl.append(0)
	i = 1
	while(i < n):
		bl[i] = cmp(s,0,i)
		i += 1
	for elem in bl:
		print(elem)
'''
	

filename = "T6.txt"
f = open(filename)
t = f.read()
for s in t:
	if (s == symbol):
		print("Текс содержит недопустимый символ - " + symbol)
		exit(0)
p = "Chapter"
for s in p:
	if (s == symbol):
		print("Образец содержит недопустимый символ - " + symbol)
		exit(0)	
pt = ' ' + p + symbol + t
pt2 = p + symbol + t
print("Текст T записан в файле: " + filename)
print("Искомый образец P: " + p)
print()
print("Метод вычисления массива граней префиксов:")
t1 = time()
maxborderarray(pt)
t2 = time()
m = len(p); flag = False; k = 0
for i, elem in enumerate(br):
	if (elem == m):
		k += 1
		flag = True
		#pos = i - 2*m
		#print("P входит в T в позиции: " + str(pos))
if (not flag):
	print("Вхождений образца P в текст T не найдено!")
else:
	print("Кол-во вхождений образца P в текст T: " + str(k))
print("Время работы: " + str(t2 - t1) + " sec.")
print(); k = 0
print("Метод вычисления массива блоков:")
t1 = time()
blockarray(pt2)
t2 = time()
m = len(p); flag = False 
for i, elem in enumerate(bl):
	if (elem == m):
		k += 1
		flag = True
		#pos = i - m - 1
		#print("P входит в T в позиции: " + str(pos))
if (not flag):
	print("Вхождений образца P в текст T не найдено!")
else:
	print("Кол-во вхождений образца P в текст T: " + str(k))
print("Время работы: " + str(t2 - t1) + " sec.")
f.close()
exit(0)





