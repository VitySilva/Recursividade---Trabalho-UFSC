def hanoi(n, origem, destino, auxiliar):
    if n == 1: 
        print(f"Mover disco 1 de {origem} para {destino}")
    else:
        hanoi(n - 1, origem, auxiliar, destino)
    
        print(f"Mover disco {n} de {origem} para {destino}")
        hanoi(n - 1, auxiliar, destino, origem)


print("Solução para 3 discos:")
hanoi(3, 'A', 'C', 'B')
