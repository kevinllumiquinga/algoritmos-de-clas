def numeroMayor(a,b,c):
    if a>b and a>c:
        print("el numero mayor es: ",a)
        return a
    elif b>a and b>c:
        print("el numero mayor es: ",b)
        return b
    elif c>a and c>b:
        print("el numero mayor es: ",c)
        return c

var1=int(input("ingrese A: "))
var2=int(input("ingrese b: "))
var3=int(input("ingrese c: "))
print(numeroMayor(var1, var2, var3))

