
from time import time


simpleArray = []
divideArray = []

def simpleNumber(I):     # решето Эратосфена
	for i in range(I):
		divideArray.append(0)

	for i in range(2, I):
		if (divideArray[i] == 0):
			divideArray[i] = i
			simpleArray.append(i)
		for p in simpleArray:
			if (p <= divideArray[i] and p*i < I):
				divideArray[p*i] = p
	return simpleArray[len(simpleArray)-1]


I = 10000
q = simpleNumber(I)


def Hash(binStr, m):
	h = int(binStr[0])
	for i in range(m-1):
		t = h * 2 % q
		h = t + int(binStr[i+1])
	return h


def karp_rabin(binP, binT):
	n = len(binT)
	m = len(binP)
	heshTab = []
	heshTab.append(Hash(binT[0:m], m))
	for i in range(1, n-m+1):
		heshTab.append((2*heshTab[i-1] % q) - (pow(2,m) % q) * int(binT[i-1]) + int(binT[i + m - 1]) % q)

	k = 0
	hesh_P = Hash(binP, m)
	for i in range(n-m+1):
		if hesh_P == heshTab[i] and binP in binT[i:i+m]:
			k += 1
	return k


def main():
	filename = "T6.txt"
	f = open(filename)
	T = f.read()
	binT = str(''.join(format(ord(x), 'b') for x in T))
	P = "Chapter"
	binP = str(''.join(format(ord(x), 'b') for x in P))

	print("Текст T записан в файле: " + filename)
	print("Искомый образец P: " + P)
	print()

	print("Алгоритм Карпа-Рабина:")
	t1 = time()
	count = karp_rabin(binP, binT)
	t2 = time()
	if (count == 0):
		print("Вхождений образца P в текст T не найдено!")
	else:
		print("Кол-во вхождений образца P в текст T: " + str(count))
	print("Время работы: " + str(t2 - t1) + " sec.")


if __name__ == '__main__':
	main()