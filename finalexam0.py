def calcPi(n):
    total = 0
    for i in range(1,n+1):
        hang = ((-1)**(i+1))/(2*i-1)
        total += hang

    total *= 4
    return total

print(" i               m(i)")
for i in range(1, 902, 100):
    print("{0:3d}          {1:9.4f}".format(i,calcPi(i)))
