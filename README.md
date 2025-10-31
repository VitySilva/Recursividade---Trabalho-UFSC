RELATÓRIO

CÁLCULO FATORIAL RECURSIVO

O caso base ocorre quando n é igual a 0 ou 1. Nesse ponto, a função retorna 1, interrompendo a recursão e evitando chamadas infinitas.
O passo recursivo ocorre da seguinte forma: para valores de n > 1, o problema é reduzido para um subproblema menor: fatorial(n) = n * fatorial(n - 1). 
Assim, cada chamada depende do resultado da chamada anterior, até chegar ao caso base.

Rastreamento para n = 4:
fatorial(4)
= 4 * fatorial(3)
    = 4 * (3 * fatorial(2))
        = 4 * (3 * (2 * fatorial(1)))
            = 4 * (3 * (2 * 1))
= 4 * 3 * 2 * 1 = 24


BUSCA BINÁRIA RECURSIVA

A busca binária é um algoritmo eficiente para localizar um valor dentro de uma lista ordenada. Ela reduz o espaço de busca pela metade a cada chamada recursiva.
O funcionamento só ocorre corretamente se a lista estiver ordenada, pois a divisão do espaço de busca depende da comparação entre o valor procurado e o elemento do meio, o que evidencia a relevância da lista ordenada.
Ao analisar o passo recursivo, é importante entender que a cada chamada, o problema é reduzido à metade da lista — se o valor buscado for menor, a busca continua à esquerda; se for maior, à direita.
Com relação aos casos base, o caso de sucesso ocorre quando o valor no índice do meio é igual ao valor procurado. Além disso, configura-se caso de falha quando o limite inicial ultrapassa o limite final (início > fim), indicando que o valor não está presente na lista.


TORRES DE HANÓI

O problema das Torres de Hanói é um exemplo clássico que demonstra o poder da recursividade. O objetivo é mover uma pilha de discos de um pino de origem para um pino de destino, utilizando um pino auxiliar, sem nunca colocar um disco maior sobre um menor.
A lógica dos três passos é o princípio que orienta o funcionamento do algoritmo recursivo das Torres de Hanói. Ela divide o problema maior (mover n discos) em três etapas menores e mais simples, repetidas recursivamente até chegar ao caso base (n = 1).
Sabendo-se disso, a lógica dos três passos segue o seguinte esquema:
•	Mover os n−1 discos superiores da torre de origem para o pino auxiliar;
•	Mover o disco maior (n) da origem para o destino;
•	Mover os n−1 discos do pino auxiliar para o destino.

No que se refere ao caso base, este, ocorre quando há apenas um disco (n == 1), que pode ser movido diretamente da origem para o destino. A partir daí a recursão começa a se desenrolar, resolvendo os passos pendentes, como pode ser observado no rastreamento abaixo:
hanoi(3, A, C, B)
→ hanoi(2, A, B, C)
    → hanoi(1, A, C, B)
        Mover disco 1 de A para C
    Mover disco 2 de A para B
    → hanoi(1, C, B, A)
        Mover disco 1 de C para B
Mover disco 3 de A para C
→ hanoi(2, B, C, A)
    → hanoi(1, B, A, C)
        Mover disco 1 de B para A
    Mover disco 2 de B para C
    → hanoi(1, A, C, B)
        Mover disco 1 de A para C.
