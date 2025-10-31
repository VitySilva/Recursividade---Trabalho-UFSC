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


print("=== BUSCA BINÁRIA RECURSIVA ===")


entrada = input("Digite os números da lista em ordem crescente, separados por espaço: ")
lista = [int(x) for x in entrada.split()]
valor = int(input("Digite o valor que deseja procurar: "))

resultado = busca_binaria(lista, valor, 0, len(lista) - 1)

if resultado != -1:
    print(f"O valor {valor} foi encontrado no índice {resultado}.")
else:
    print(f"O valor {valor} não foi encontrado na lista.")
