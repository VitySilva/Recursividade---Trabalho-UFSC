def busca_binaria(lista, valor, inicio, fim):
    if inicio > fim:  
        return -1
    meio = (inicio + fim) // 2

    if lista[meio] == valor:  
        return meio
    elif valor < lista[meio]:  
        return busca_binaria(lista, valor, inicio, meio - 1)
    else: 
        return busca_binaria(lista, valor, meio + 1, fim)


valores = [1, 3, 5, 7, 9, 11]
resultado = busca_binaria(valores, 7, 0, len(valores) - 1)
print("Índice do valor 7:", resultado)