from time import time

def SearchShiftAnd(p,t):
    V = []
    n = len(t)
    m = len(p)
    k = 0
    for i in range(255):
        V.append(0)
    for i in range(m):
        V[ord(p[i])] = V[ord(p[i])] | (1 << (m-i-1))
    first = 1 << (m-1)
    R = 0
    for i in range(n):
        R = ((R >> 1) | first) & V[ord(t[i])]
        if R & 1:
            k += 1
    return k

def main():
    filename = "T.txt"
    f = open(filename)
    t = f.read()
    p = "a"
    t1 = time()
    count = SearchShiftAnd(p, t)
    t2 = time()
    print("Алгоритм Shift-And")
    print ("Количество вхождений образца P в текс T: " + str(count))
    print("Время работы алгоритма: " + str(t2 - t1))
    exit(0)

if __name__ == '__main__':
    main()
