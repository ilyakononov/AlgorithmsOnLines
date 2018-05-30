from time import time
br = [0,0]
brs = [0,0]
alphabet = ['a', 'b', 'c', 'd', 'e']

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


def make_brsa(p):
    n = len(p)
    m = len(alphabet)
    array = [[0] * m for i in range(n)]
    array.insert(0, alphabet)
    i = 1
    while i <= n:
        sp = list(' ' + p[:i+1] + ' ')
        for j in range(m):
            sp[brs[i]+1] = array[0][j]
            maxborderarray(sp)
            array[i][j] = br[i]
            for elem in br:
                print(elem, end=' ')
            print()
            del br[2:]
        sp.clear()
        i += 1

    for i in range(n+1):
        for j in range(m):
            print(array[i][j], end=' ')
        print()
    print(brs)
    return array

def kmp(t,p):
    n = len(t)
    m = len(p)
    k = 0
    s = ' ' + p + ' '
    maxborderarray(s)
    #for elem in br:
     #   print(elem,end=' ')
    #print()
    brst(s)
    del br[2:]
    brsa = make_brsa(p)
    i = 1; q = 0
    while (i < n):
        while (q > 0 and s[q+1] != t[i]):
            q = brsa[q][brsa[0].index(s[q+1])] + 1
            break
        if (s[q+1] == t[i]):
            q += 1
        if (q == m):
            k += 1
            q = brs[m]
        i += 1
    return k


filename = "T.txt"
f = open(filename)
t = ' ' + f.read()
p = "ab"
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


