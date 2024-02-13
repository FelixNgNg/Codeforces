soal = int(input(""))
para = 0
for i in range(soal):
    pvto = input('').split()
    pvt = [eval(s) for s in pvto]
    
    
  
    a = pvt[0]
    b = pvt[1]
    c = pvt[2]


    if a+b+c > 1:
        para=para + 1
    

print(para)

