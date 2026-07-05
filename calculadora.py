def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        raise ValueError("Nao e possivel dividir por zero")
    return a / b


if __name__ == "__main__":
    print("Soma: 2 + 3 =", soma(2, 3))
    print("Subtracao: 5 - 2 =", subtracao(5, 2))
    print("Multiplicacao: 4 * 3 =", multiplicacao(4, 3))
    print("Divisao: 10 / 2 =", divisao(10, 2))
