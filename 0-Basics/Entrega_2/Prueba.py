Nombre_distrito = input("Introduce nombre del distrito ")
Superficie = int(input("Introduce la superficie "))

if Nombre_distrito == "Retiro":
    print("Distrito Retiro")
    if Superficie > 100:
        print("El precio de la casa es: 1000")
    else:
        print("El precio de la casa es: 500")
else:
    print("Otro distrito")
