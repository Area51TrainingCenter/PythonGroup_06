def es_primo(n):
    for numero in range(2, n):
        if n % numero == 0:
            return False

    return True

primos = [n for n in range(101) if es_primo(n)]
print(primos)
