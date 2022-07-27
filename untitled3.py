error=False
var1=int(input("si desea obtener la hora sumando los segundos adicionales digite culaquier numero menos el cero(0), cuando ya no rrequiera utilizar el programa digite el (0): "))
while var1!=0:
    print("continue")
    
    hora=int(input("ingrese una hora hh: "))
    while hora>23 or hora <0:
        print("numero fuera de rango, ingrese nuevamente.")
        hora=int(input("ingrese una hora hh: "))
    if hora>23 or hora <0:
        print("dato de hora no es correcto")
        error=True
    print("continuar")

    minutos=int(input("ingrese un valor en minutos: "))
    while minutos>59 or minutos<0:
        print("numero fuera de rango, ingrese nuevamente.")
        minutos=int(input("ingrese un valor en minutos: "))
    if minutos>59 or minutos<0:
        print("daro de minutos no es correcto")
        erro=True
    print("continuar")

    segundos=int(input("ingrese una valor en segundos: "))
    while segundos>59 or segundos<0:
        print("numero fuera de rango, ingrese nuevamente.")
        segundos=int(input("ingrese una valor en segundos: "))
    if segundos>59 or segundos<0:
        print("daro de segundos no es correcto")
        error=True
    print("continue")

    if error==False:
        nuevo=int(input("ingrese el valor de los segundos extra: "))
        while nuevo<0:
            print("numero negativo, ingrese nuevamente")
            nuevo=int(input("ingrese el valor de los segundos extra: "))
        print("continuar")    
        if nuevo<0:
            print("el valor de los segundos extra son invalidos")
        else:
            print("puede continuar")
            segundosn=(hora*3600)+(minutos*60)+segundos
            suma=nuevo+segundosn
            hh=int(suma/3600)
            mm=int((suma/60)-(hh*60))
            ss=int((suma-(mm*60)-(hh*3600)))
            print(hh,":",mm,":",ss)
    else:
        print("fin de programa")
    var1=int(input("si desea obtener la hora sumando los segundos adicionales digite (1), cuando ya no rrquiera digite culaquier numero diferente de (1): "))
print("fin")   




