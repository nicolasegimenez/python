a=7
b=5
c=3

for i in range(0,7):
    if a>b>c:
        print("a = "+ str(a)," b = " +str(b), " c = "+str(c))
        c -= 1
        b -= 1
        a -=1