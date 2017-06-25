def es_primo(n):
    for numero in range(2, n):
        if n % numero == 0:
            return False

    return True

primos = filter(lambda n: not es_primo(n), range(101))
print(list(primos))
