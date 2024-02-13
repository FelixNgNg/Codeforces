onel = input("").split()
twol = input("").split()
threel = input("").split()
fourl = input("").split()
fivel = input("").split()
one = [eval(i) for i in onel]
two = [eval(i) for i in twol]
three = [eval(i) for i in threel]
four = [eval(i) for i in fourl]
five = [eval(i) for i in fivel]

if (one[0]== 1 or one[4]== 1 or five[0]== 1 or five[4] == 1):
    print(int('4'))
elif (one[1]== 1 or one[3]== 1 or two[0]== 1 or two[4]== 1 or four[0]== 1 or four[4]== 1 or five[1]== 1 or five[3] == 1):
    print(int('3'))
elif (one[2]== 1 or two[1]== 1 or two[3] == 1 or three[0]== 1 or three[4]== 1 or four[1]== 1 or four[3]== 1 or five[2] == 1):
    print(int('2'))
elif (three[2] == 1):
    print(int('0'))
else:
    print(int('1'))
