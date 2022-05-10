def factores(numero):
    # La variable 'numero' es el numero del cual queremos los factores
    if numero % 2 == 0:
        num = int(numero / 2)
        # La variable 'num' es la mitad del numero inicial para poder encontrar los factores
    else:
        num = int(numero / 2 + 1)

    numeros = range(1, num +1)
    # La variable numeros es un rango del 1 a la mitad de nuestro numero para poder
    # conseguir los factores
    factores_list = []
    # En la lista factores list se almacenaran todos los numeros
    for i in numeros:
        # Este for almacenará los factores en la lista si al dividir el numero entre el posible
        # factor el residuo sea 0
        if numero % i == 0:
            factores_list.append(i)
    factores_list.append(numero)
    # se agrega el numero base al final porque el numero siempre será un factor de sí mismo
    return print(factores_list)


if __name__ == "__main__":
    numero = int(input('Escoge un numero: '))
    factores(numero)