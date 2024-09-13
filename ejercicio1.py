def busqueda_fuerza_bruta(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

lista = [1, 2, 3, 4, 5, 6]
objetivo = 9
resultado = busqueda_fuerza_bruta(lista, objetivo)
print(f'Índice del objetivo (fuerza bruta): {resultado}')