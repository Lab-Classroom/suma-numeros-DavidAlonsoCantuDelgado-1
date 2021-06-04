def main():
    #escribe tu código abajo de esta línea
    suma = 0
    num = int(input("Teclea un número: "))
    while num != 0:
        suma = suma + num
        num = int(input("Teclea un número: "))

    print("La suma de todos los números es: {}".format(suma))

main()
