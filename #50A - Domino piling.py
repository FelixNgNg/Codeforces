mN = input("").split()
m = int(mN[0])
n = int(mN[1])
l = m * n
if l%2 == 0:
    print(int((l/2)))
elif l%2 == 1:
    print(int((l-1)/2))
