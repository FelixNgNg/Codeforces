n = int(input(''))
x = 0

for i in range(n):
    ror = input("")
    if ror == "X++":
        x = x + 1
    elif ror == "--X":
        x = x - 1
    elif ror == "++X":
        x = x + 1
    elif ror == "+X+":
        x = x + 1
    elif ror == "X--":
        x = x - 1
    elif ror == "-X-":
        x = x - 1

        
print(x)
