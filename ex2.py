def pertence_a_fibonacci(numero):

    a, b = 0, 1

    if numero == 0 or numero == 1:
        return True


    while b < numero:
        a, b = b, a + b

        if b == numero:
            return True

    return False


numero = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))

if pertence_a_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} NÃO pertence à sequência de Fibonacci.")