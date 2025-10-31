def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


print("Fatorial de 4 =", fatorial(4))
