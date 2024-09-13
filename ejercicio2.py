def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

lista_ordenada = [1, 2, 4, 6, 8, 10, 12, 14]
objetivo = 20
resultado = busqueda_binaria(lista_ordenada, objetivo)

if resultado != -1:
    print(f"Este elemento ha sido encontrado en el índice {resultado}.")
else:
    print("Este elemento no ha sido encontrado.")