peserJuara = input("").split()
n = int(peserJuara[0])
k = int(peserJuara[1])
lolos = 0

a = input("").split()
b = [eval(p) for p in a]
b.sort()
b.reverse()
c = len(b)
kanya = b[k-1]

for i in range(c):
    if b[i] >= kanya and b[i] > 0:
        lolos = lolos + 1

print(lolos)
