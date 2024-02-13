x = int(input(''))
lis = []
for i in range(x):
    pol = input("")
    lis.append(pol)

for o in range (x):
    lol = o
    katanya = lis[lol]
    pert = katanya[0]
    akhir = katanya[-1]
    panj = int(len(lis[lol]))
    if panj > 10:
        panja = str(panj - 2)
        print(pert + panja + akhir)
    else:
        print(katanya)
    
