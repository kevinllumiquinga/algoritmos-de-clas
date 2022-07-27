def transformacion(a):
    gra=(a*(180.0/100.0))+32
    return gra

var1=float(input("Grados Celcius: "))
print("Grados Fahrenheit:",transformacion(var1))

    